#!/usr/bin/env python3
"""Build the README demo, one SVG per scene, from the scene files in docs/demo/. Standard library only.

    python3 tools/demo_svg.py    the first scene file -> docs/demo-hard.svg, the second -> docs/demo-easy.svg

A scene file, docs/demo/<n>-<title>.txt, holds one exchange; files are taken in name order. Its
messages are separated by lines holding only "---" and alternate user and kit, the user first.
Lines starting with "#" at the top note the source and are not shown. The file name gives the
plain grey title line at the top ("1-hard-to-undo" -> "Hard to undo"). The kit's last message,
its answer, fills the right pane; the others stay on the left as a conversation. The texts come
from eval runs, keeping whole sentences and lines. This script only lays them out (word wrap with
a hanging indent, spacing, colors, `code`) and animates them with CSS, each SVG looping on its
own scene. With reduced motion, or where animation does not run, the scene shows complete and still.
"""
import argparse
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

ROOT = Path(__file__).resolve().parent.parent
SCENES = ROOT / "docs" / "demo"
OUTPUTS = (ROOT / "docs" / "demo-hard.svg", ROOT / "docs" / "demo-easy.svg")  # one per scene file, in name order

# Layout, in px. GitHub shows a README about 830 px wide, so the text renders near these sizes.
W = 840
PAD = 16
TITLE = 26                   # baseline of the title line
TOP = 42                     # first message, below the title
LEFT_W = 344                 # the conversation
RIGHT_X = PAD + LEFT_W + 14  # the answer
RIGHT_W = W - PAD - RIGHT_X
FS, LH = 13.5, 19.5          # body font size and line height
BUBBLE = (11, 8)             # padding inside a message: x, y
CARD = (16, 12)              # padding inside the answer: x, y
GAP = 10                     # space before a section of the answer
HANG = 14                    # indent of the wrapped lines of an answer line
LIST = 20                    # indent of a list item's text

# Timing, in seconds.
CPS = 120                    # typing speed of the user's messages
FADE = 0.3
READ = 3.5                   # pause after a kit message on the left
STAGGER = 0.3                # between the lines of the answer
HOLD = (8.0, 14.0)           # the complete answer stays 1 s per 50 characters, within these bounds

FG, MUTED, BORDER, CANVAS = "#1f2328", "#59636e", "#d0d7de", "#f6f8fa"
BLUE, GREEN, RED, ORANGE, PURPLE, AMBER = "#0969da", "#1a7f37", "#d1242f", "#bc4c00", "#8250df", "#9a6700"
USER_BG, USER_EDGE, MARK, CODE_BG = "#ddf4ff", "#b6e3ff", "#ffeb99", "#eff1f3"
SANS = "Helvetica, Arial, 'Liberation Sans', sans-serif"  # same letter widths on every system
MONO = "Menlo, Consolas, 'Liberation Mono', 'DejaVu Sans Mono', monospace"  # 0.6 em or narrower
CODE_PAD = 3                 # inside a `code` span's background, on each side

# Helvetica advance widths in 1/1000 em, ASCII 32-126; Arial and Liberation Sans share them.
REGULAR = """278 278 355 556 556 889 667 191 333 333 389 584 278 333 278 278 556 556 556 556 556 556
556 556 556 556 278 278 584 584 584 556 1015 667 667 722 722 667 611 778 722 278 500 667 556 833 722
778 667 778 722 667 611 722 667 944 667 667 611 278 278 278 469 556 333 556 556 500 556 556 278 556
556 222 222 500 222 833 556 556 556 556 333 500 278 556 500 722 500 500 500 334 260 334 584"""
BOLD = """278 333 474 556 556 889 722 238 333 333 389 584 278 333 278 278 556 556 556 556 556 556 556
556 556 556 333 333 584 584 584 611 975 722 722 722 722 667 611 778 722 278 556 722 611 833 722 778
667 778 722 667 611 722 667 944 667 667 611 333 278 333 584 556 333 556 611 556 611 556 333 611 611
278 278 556 278 889 611 611 611 611 389 556 333 611 556 778 556 556 500 389 280 389 584"""
EXTRA = {"·": 278, "–": 556, "—": 1000, "←": 1000, "•": 350, "’": 222, "“": 333, "”": 333}
WIDTHS = {bold: {**dict(zip(map(chr, range(32, 127)), map(int, table.split()))), **EXTRA}
          for bold, table in ((False, REGULAR), (True, BOLD))}

STYLE = {  # name: (monospace, size, bold, color)
    "text": (False, FS, False, FG),
    "mark": (False, FS, False, FG),       # words of the plan that the answer quotes
    "bold": (False, FS, True, FG),
    "muted": (False, 12.5, False, MUTED),
    "code": (True, 12.5, False, FG),
    "cite": (False, FS, False, BLUE),     # [L2 ← "…"]
    "quote": (False, FS, False, BLUE),    # the quoted words, marked like the plan's
    "oneway": (False, FS, True, RED),
    "twoway": (False, FS, True, GREEN),
    "go": (False, 22, True, GREEN),
    "test": (False, FS, True, GREEN),
    "risk": (False, FS, True, ORANGE),
    "trip": (False, FS, True, PURPLE),
    "door": (False, FS, True, AMBER),
    "watch": (False, FS, True, PURPLE),
    "who": (False, 11.5, True, MUTED),    # speaker names
    "title": (False, 12.5, False, MUTED),  # the scene's name: plain text, nothing that looks clickable
}
LABELS = {"Cheapest test:": "test", "Risks:": "risk", "Tripwires:": "trip",
          "Door closes if:": "door", "Watch:": "watch"}
SECTIONS = ("Cheapest test:", "Risks:", "Tripwires:", "Go.", "Door closes if:")
NO_BREAK_BEFORE = re.compile(r"[·—–←%]+")  # never start a line with these, nor with a number
NO_BREAK_AFTER = {"a", "an", "the"}         # never end a line with these


def width(text, style):
    """Advance width in px; a `code` span counts its background's padding."""
    mono, size, bold, _ = STYLE[style]
    if mono:
        return len(text) * 0.602 * size + 2 * CODE_PAD
    return sum(WIDTHS[bold].get(ch, 1000) for ch in text) * size / 1000


def code(text, style="text"):
    """Split `code` spans out of a run of text."""
    return [(part, "code" if i % 2 else style) for i, part in enumerate(text.split("`")) if part]


def kit_line(line):
    """Style one line of the kit -> (marker, runs, gap before)."""
    gap = line.startswith(SECTIONS)
    m = re.match(r"(jamais-vu check)( · )(one-way|two-way door)(.*)$", line)
    if m:
        door = "oneway" if m[3] == "one-way" else "twoway"
        return None, [(m[1], "bold"), (m[2], "muted"), (m[3], door)] + code(m[4]), gap
    if line.startswith("consulted:"):
        return None, [(line, "muted")], gap
    if line == "Go.":
        return None, [(line, "go")], gap
    for label, style in LABELS.items():
        if line.startswith(label):
            return None, [(label, style)] + code(line[len(label):]), gap
    m = re.match(r'(\d+\.) (\[\S+ ← ")(.*?)("\])(.*)$', line)
    if m:
        return (m[1], "risk"), [(m[2], "cite"), (m[3], "quote"), (m[4], "cite")] + code(m[5]), gap
    m = re.match(r"(\(\d\)) (.*)$", line)
    if m:
        return (m[1], "bold"), code(m[2]), gap
    if line.startswith("- "):
        return ("•", "trip"), code(line[2:]), gap
    return None, code(line), gap


def marked(text, quotes):
    """Runs of a user message, with the phrases the answer quotes styled "mark"."""
    runs = [(text, "text")]
    for quote in quotes:
        at = text.lower().find(quote.lower())
        if at >= 0:
            runs = [(text[:at], "text"), (text[at:at + len(quote)], "mark"), (text[at + len(quote):], "text")]
    return [r for r in runs if r[0]]


def words(runs):
    """Split styled runs at spaces, never inside `code` -> [style of the space before or None, [(text, style)]]."""
    out, space = [], None
    for text, style in runs:
        for ch in text:
            if ch == " " and style != "code":
                space = style
            elif space or not out:
                out.append([space, [(ch, style)]])
                space = None
            elif out[-1][1][-1][1] == style:
                out[-1][1][-1] = (out[-1][1][-1][0] + ch, style)
            else:
                out[-1][1].append((ch, style))
    return out


def fill(ws, avail, hang, strict):
    """Greedy line filling; words that must stay together move as one unit."""
    units, prev = [], ""
    for word in ws:
        text = "".join(t for t, _ in word[1])
        keep = (NO_BREAK_BEFORE.fullmatch(text) or text[:1].isdigit() or (text == "min" and prev[-1:].isdigit())
                or (strict and prev.lower() in NO_BREAK_AFTER))
        if units and keep:
            units[-1].append(word)
        else:
            units.append([word])
        prev = text

    def cost(unit, fresh):
        return sum((width(" ", sp) if sp and (k or not fresh) else 0) + sum(width(t, s) for t, s in parts)
                   for k, (sp, parts) in enumerate(unit))

    lines, used = [[]], 0.0
    for unit in units:
        indent = hang if len(lines) > 1 else 0.0
        if lines[-1] and indent + used + cost(unit, False) > avail * 0.97:  # 3 % spare for other fonts
            lines.append([])
            used = 0.0
        used += cost(unit, not lines[-1])
        lines[-1].extend(unit)
    return lines


def wrap(runs, avail, hang=0.0):
    """Wrap at word boundaries -> [(segments [x, text, style], line width)]. Lines end on "a" or
    "the" only when keeping it with its noun would take one more line."""
    ws = words(runs)
    strict, loose = fill(ws, avail, hang, True), fill(ws, avail, hang, False)
    lines = strict if len(strict) <= len(loose) else loose
    placed = []
    for n, line in enumerate(lines):
        x, segs = (hang if n else 0.0), []
        for k, (sp, parts) in enumerate(line):
            for j, (t, s) in enumerate(parts):
                lead = " " if (k and sp and j == 0) else ""
                if segs and segs[-1][2] == s != "code":
                    segs[-1][1] += lead + t
                    x += width(lead + t, s)
                else:
                    x += width(lead, sp) if lead else 0
                    segs.append([x, t, s])
                    x += width(t, s)
        placed.append((segs, x))
    return placed


class Timeline:
    """Collect the timed effects; their CSS is written once the loop length is known."""

    def __init__(self):
        self.effects = {}

    def _name(self, key):
        if key not in self.effects:
            self.effects[key] = f"{key[0][0]}{len(self.effects)}"
        return self.effects[key]

    def show(self, start, end):
        """Class of an element visible from start to end, and always when nothing plays."""
        return self._name(("show", round(start, 2), round(end, 2)))

    def type(self, start, end, distance, steps):
        """Class of a cover that slides off a line of text in steps, like typing."""
        return self._name(("type", round(start, 2), round(end, 2), round(distance, 1), steps))

    def css(self, total):
        def pc(t):
            return f"{max(0.0, min(100.0, 100 * t / total)):.3f}%"
        out = []
        for key, name in self.effects.items():
            kind, a, b, base = key[0], key[1], key[2], ""
            if kind == "show":
                frames = (f"0%,{pc(a)}{{opacity:0}}{pc(a + FADE)},{pc(b)}{{opacity:1}}"
                          f"{pc(b + FADE)},100%{{opacity:0}}")
            else:
                frames = (f"0%,{pc(a)}{{transform:translateX(0);animation-timing-function:steps({key[4]},end)}}"
                          f"{pc(b)},100%{{transform:translateX({key[3]}px)}}")
                base = f"transform:translateX({key[3]}px);"
            out.append(f"@keyframes {name}{{{frames}}}.{name}{{{base}animation:{name} {total:.2f}s linear infinite}}")
        return "\n".join(out)


def text_lines(placed, x0, y0, line_h=LH):
    """SVG of wrapped lines -> (background marks as (kind, rect), text elements)."""
    backs, texts = [], []
    for n, (segs, _) in enumerate(placed):
        size = max(STYLE[s][1] for _, _, s in segs)
        base = y0 + n * line_h + line_h / 2 + size * 0.36
        spans = []
        for x, t, s in segs:
            w = width(t, s)
            if s == "code":
                backs.append((s, f'<rect x="{x0 + x:.1f}" y="{base - 11:.1f}" width="{w:.1f}" '
                                 f'height="15" rx="3" fill="{CODE_BG}"/>'))
                x += CODE_PAD
            elif s in ("quote", "mark"):
                backs.append((s, f'<rect x="{x0 + x - 2:.1f}" y="{base - 12.5:.1f}" width="{w + 4:.1f}" '
                                 f'height="17" rx="3" fill="{MARK}"/>'))
            cls = "" if s in ("text", "mark") else f' class="{s}"'
            spans.append(f'<tspan x="{x0 + x:.1f}"{cls}>{escape(t)}</tspan>')
        texts.append(f'<text y="{base:.1f}">{"".join(spans)}</text>')
    return backs, texts


def paragraph(line, avail):
    """Wrap one line of the kit -> (marker, placed lines, gap before, line height)."""
    marker, runs, gap = kit_line(line)
    if marker:
        return marker, wrap(runs, avail - LIST), gap, LH
    if runs[0][1] == "go":
        return None, wrap(runs, avail), gap, 30.0
    return None, wrap(runs, avail, HANG), gap, LH


def draw_paragraph(para, x0, y0):
    """-> (background marks, text elements, height) of one wrapped paragraph."""
    marker, placed, _, lh = para
    backs, texts = text_lines(placed, x0 + (LIST if marker else 0), y0, lh)
    if marker:
        texts.insert(0, text_lines([([[0.0, marker[0], marker[1]]], 0)], x0, y0, lh)[1][0])
    return backs, texts, len(placed) * lh


def scene_svg(msgs, tl):
    """One scene -> (svg, end time, lowest y). Messages on the left, the answer on the right."""
    left, answer = msgs[:-1], msgs[-1].splitlines()
    quotes = [q for line in answer for q in re.findall(r'← "(.*?)"\]', line)]
    timed, marks, t, y = [], [], 0.4, TOP  # timed: (start, svg parts shown until the scene ends)
    for i, msg in enumerate(left):
        user = i % 2 == 0
        inner = LEFT_W - 2 * BUBBLE[0]
        if user:
            paras = [(None, wrap(marked(p, quotes if i == 0 else []), inner), False, LH) for p in msg.splitlines()]
        else:
            paras = [paragraph(p, inner) for p in msg.splitlines()]
        top = y + 16
        h = sum(len(p[1]) * p[3] for p in paras) + 2 * BUBBLE[1]
        fill, edge = (USER_BG, USER_EDGE) if user else ("#ffffff", BORDER)
        parts = [f'<text x="{PAD + 2}" y="{y + 11}" class="who">{"You" if user else "jamais-vu"}</text>',
                 f'<rect x="{PAD}" y="{top}" width="{LEFT_W}" height="{h:.1f}" rx="10" fill="{fill}" stroke="{edge}"/>']
        if i == 0:
            parts.append("\0marks\0")  # the quoted words' marks go under the text, shown later
        covers, ly, typing = [], top + BUBBLE[1], t + 0.25
        for para in paras:
            backs, texts, ph = draw_paragraph(para, PAD + BUBBLE[0], ly)
            for kind, rect in backs:
                (marks if kind == "mark" else parts).append(rect)
            parts += texts
            if user:
                for n, (segs, lw) in enumerate(para[1]):
                    chars = max(1, sum(len(s[1]) for s in segs))
                    span = lw * 1.05 + 8
                    cls = tl.type(typing, typing + chars / CPS, span, chars)
                    covers.append(f'<rect x="{PAD + BUBBLE[0] - 2}" y="{ly + n * LH:.1f}" width="{span:.1f}" '
                                  f'height="{LH}" fill="{USER_BG}" class="{cls}"/>')
                    typing += chars / CPS
            ly += ph
        if covers:
            parts.append(f'<clipPath id="k{i}"><rect x="{PAD + 1}" y="{top + 1}" width="{LEFT_W - 2}" '
                         f'height="{h - 2:.1f}" rx="9"/></clipPath><g clip-path="url(#k{i})">{"".join(covers)}</g>')
        timed.append((t, parts))
        t = typing + 0.5 if user else t + READ
        y = top + h + 12
    left_low = y - 12

    paras = [paragraph(line, RIGHT_W - 2 * CARD[0]) for line in answer]
    top = TOP + 16
    h = sum(len(p[1]) * p[3] + (GAP if p[2] else 0) for p in paras) + 2 * CARD[1]
    door = RED if " · one-way" in answer[0] else GREEN
    timed.append((t, [
        f'<text x="{RIGHT_X + 2}" y="{TOP + 11}" class="who">jamais-vu</text>',
        f'<clipPath id="a"><rect x="{RIGHT_X}" y="{top}" width="{RIGHT_W}" height="{h:.1f}" rx="10"/></clipPath>',
        f'<rect x="{RIGHT_X}" y="{top}" width="{RIGHT_W}" height="{h:.1f}" rx="10" fill="#ffffff" stroke="{BORDER}"/>',
        f'<rect x="{RIGHT_X}" y="{top}" width="5" height="{h:.1f}" fill="{door}" clip-path="url(#a)"/>']))
    ly, chars, quote_at = top + CARD[1], 0, None
    for k, para in enumerate(paras):
        ly += GAP if para[2] else 0
        at = t + k * STAGGER
        backs, texts, ph = draw_paragraph(para, RIGHT_X + CARD[0], ly)
        if quote_at is None and any(kind == "quote" for kind, _ in backs):
            quote_at = at
        timed.append((at, [rect for _, rect in backs] + texts))
        ly += ph
        chars += len(answer[k])
    end = t + (len(paras) - 1) * STAGGER + FADE + min(HOLD[1], max(HOLD[0], chars / 50))

    svg = "".join(f'<g class="{tl.show(at, end)}">{"".join(parts)}</g>' for at, parts in timed)
    shown = f'<g class="{tl.show(quote_at, end)}">{"".join(marks)}</g>' if marks and quote_at else ""
    return svg.replace("\0marks\0", shown), end, max(left_low, top + h)


def read_scene(path):
    """-> (title, messages) of a scene file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    while lines and lines[0].startswith("#"):
        lines.pop(0)
    title = re.sub(r"^\d+-", "", path.stem).replace("-", " ").capitalize()
    return title, [m.strip("\n") for m in "\n".join(lines).split("\n---\n")]


def build(path):
    """One scene file -> (svg, height, loop length): a title line, then the scene, looping on its own."""
    title, msgs = read_scene(path)
    tl = Timeline()
    body, end, low = scene_svg(msgs, tl)
    total, height = end + FADE + 0.2, round(low + PAD)
    styles = "".join(f".{name}{{{'font-family:' + MONO + ';' if mono else ''}font-size:{size}px;"
                     f"{'font-weight:700;' if bold else ''}fill:{color}}}"
                     for name, (mono, size, bold, color) in STYLE.items())
    css = (f"text{{font-family:{SANS};font-size:{FS}px;fill:{FG}}}{styles}\n{tl.css(total)}\n"
           f"@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" '
           f'role="img" aria-label={quoteattr("jamais-vu demo: " + title.lower())}>\n<style><![CDATA[\n{css}\n]]></style>\n'
           f'<rect x="0.5" y="0.5" width="{W - 1}" height="{height - 1}" rx="12" fill="{CANVAS}" stroke="{BORDER}"/>'
           f'<text x="{PAD + 2}" y="{TITLE}" class="title">{escape(title)}</text>\n{body}\n</svg>\n')
    return svg, height, total


def main():
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()
    scenes = sorted(SCENES.glob("*.txt"))
    if len(scenes) != len(OUTPUTS):
        sys.exit(f"expected {len(OUTPUTS)} scene files in {SCENES.relative_to(ROOT)}, found {len(scenes)}")
    for scene, out in zip(scenes, OUTPUTS):
        svg, height, total = build(scene)
        out.write_text(svg, encoding="utf-8")
        print(f"{scene.relative_to(ROOT)} -> {out.relative_to(ROOT)}: {W} x {height} px, {total:.1f} s loop, "
              f"{len(svg.encode()) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
