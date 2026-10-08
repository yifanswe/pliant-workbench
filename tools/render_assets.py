"""Render concept illustrations. Requires Pillow; no network or private data."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
FONT_DIRS = [Path('/System/Library/Fonts/Supplemental'), Path('/usr/share/fonts/truetype/dejavu')]


def font(size, bold=False):
    names = ['Arial Bold.ttf', 'DejaVuSans-Bold.ttf'] if bold else ['Arial.ttf', 'DejaVuSans.ttf']
    for folder in FONT_DIRS:
        for name in names:
            if (folder / name).exists():
                return ImageFont.truetype(str(folder / name), size)
    raise RuntimeError('Install no fonts automatically; supply Arial or DejaVu Sans.')


INK = '#1C302C'
MUTED = '#647570'
PAPER = '#F6F4EC'
GREEN = '#BCE9B1'
BLUE = '#C6D9F4'
ORANGE = '#F3D2AE'
PURPLE = '#DCD3F2'
WHITE = '#FFFEF9'
LINE = '#D5DCD1'
ARROW = '#7E9A8C'


def canvas(h, w=1600):
    im = Image.new('RGB', (w, h), PAPER)
    return im, ImageDraw.Draw(im)


def text(d, pos, value, size=24, fill=INK, bold=False):
    d.text(pos, value, font=font(size, bold), fill=fill)


def width(d, value, size, bold=False):
    return d.textbbox((0, 0), value, font=font(size, bold))[2]


def box(d, xy, fill=WHITE, radius=22, outline=None, w=2):
    d.rounded_rectangle(xy, radius, fill=fill, outline=outline, width=w)


def pill(d, x, y, label, fill=GREEN, size=18, fg=INK):
    w = width(d, label, size, True) + 28
    box(d, (x, y, x + w, y + size + 16), fill, (size + 16) // 2)
    text(d, (x + 14, y + 7), label, size, fg, True)
    return w


def line(d, xy, fill=LINE, w=2):
    d.line(xy, fill=fill, width=w)


def arrow(d, a, b, fill=ARROW, w=3, head=11):
    (x1, y1), (x2, y2) = a, b
    d.line((x1, y1, x2, y2), fill=fill, width=w)
    if x1 == x2:
        s = 1 if y2 > y1 else -1
        d.polygon([(x2, y2), (x2 - head, y2 - s * head * 1.4), (x2 + head, y2 - s * head * 1.4)], fill=fill)
    else:
        s = 1 if x2 > x1 else -1
        d.polygon([(x2, y2), (x2 - s * head * 1.4, y2 - head), (x2 - s * head * 1.4, y2 + head)], fill=fill)


def bars(d, x, y, w, n, gap=24, col='#D7DED4', thick=6):
    for j in range(n):
        line(d, (x, y + j * gap, x + w - (j % 3) * 40, y + j * gap), col, thick)


def hero():
    im, d = canvas(1000)
    pill(d, 64, 40, 'PLIANT / CONCEPT')
    text(d, (64, 98), 'Browse. Edit. With your agent.', 68, bold=True)
    text(d, (68, 188), 'One application. Information moves between reading and writing.', 29, MUTED)

    # Window frame
    X0, Y0, X1, Y1 = 64, 268, 1536, 822
    box(d, (X0 + 8, Y0 + 12, X1 + 8, Y1 + 12), '#E3E5DB', 26)
    box(d, (X0, Y0, X1, Y1), WHITE, 26, LINE)
    for i, c in enumerate(['#DB9B8A', '#E4C982', '#98BE97']):
        d.ellipse((X0 + 22 + i * 22, Y0 + 20, X0 + 34 + i * 22, Y0 + 32), fill=c)
    text(d, (X0 + 110, Y0 + 15), 'pliant  —  layout defined by the user with AI', 18, MUTED)
    line(d, (X0, Y0 + 52, X1, Y0 + 52))

    # Browse area
    bx0, bx1 = X0 + 20, X0 + 640
    top = Y0 + 70
    pill(d, bx0, top, 'BROWSE AREA', BLUE, 15)
    box(d, (bx0, top + 44, bx1, top + 80), '#F0F1EB', 10)
    text(d, (bx0 + 14, top + 52), 'example.org/article', 16, MUTED)
    text(d, (bx0 + 6, top + 104), 'Article title', 30, bold=True)
    bars(d, bx0 + 6, top + 160, 600, 3)
    # Selected text
    box(d, (bx0, top + 228, bx1 - 30, top + 296), '#FFF1B8', 8)
    text(d, (bx0 + 12, top + 238), '“The selected paragraph is', 20)
    text(d, (bx0 + 12, top + 266), ' copied into the scratch pad.”', 20)
    bars(d, bx0 + 6, top + 324, 600, 4)
    # Context menu
    mx, my = bx0 + 360, top + 300
    box(d, (mx + 4, my + 4, mx + 254, my + 128), '#E3E5DB', 12)
    box(d, (mx, my, mx + 250, my + 124), WHITE, 12, LINE)
    box(d, (mx + 8, my + 8, mx + 242, my + 44), GREEN, 8)
    text(d, (mx + 18, my + 16), 'Open in scratch pad', 18, bold=True)
    text(d, (mx + 18, my + 56), 'Ask the agent', 18)
    text(d, (mx + 18, my + 90), 'Copy', 18, MUTED)

    line(d, (bx1 + 20, Y0 + 52, bx1 + 20, Y1), LINE)
    arrow(d, (bx1 - 20, top + 262), (bx1 + 56, top + 262), INK, 4, 12)

    # Edit area (scratch pad, co-owned)
    ex0, ex1 = bx1 + 60, X1 - 20
    pill(d, ex0, top, 'EDIT AREA  ·  SCRATCH PAD', ORANGE, 15)
    pill(d, ex1 - 250, top, 'SHARED: YOU + AGENT', PURPLE, 13)
    box(d, (ex0, top + 50, ex1, top + 120), '#FFF7DC', 10)
    text(d, (ex0 + 14, top + 60), '> The selected paragraph is copied', 18, MUTED)
    text(d, (ex0 + 14, top + 88), '  into the scratch pad.', 18, MUTED)
    text(d, (ex0 + 4, top + 146), 'Why does this matter for my project?', 22)
    text(d, (ex0 + 4, top + 184), 'You can refer to', 22)
    # Placeholder filled by agent
    lx = ex0 + 4 + width(d, 'You can refer to ', 22)
    box(d, (lx, top + 180, lx + 236, top + 214), BLUE, 8)
    text(d, (lx + 10, top + 185), 'that design blog post', 20, bold=True)
    pill(d, lx + 248, top + 181, 'Revert', '#EEF0E9', 13)
    pill(d, lx + 336, top + 181, 'Other options', '#EEF0E9', 13)
    text(d, (ex0 + 4, top + 222), '(was: “this website (to be found)”)', 16, MUTED)

    # Agent proposal
    py = top + 268
    box(d, (ex0, py, ex1, py + 168), '#F4F0FC', 14, '#C7BCE6')
    pill(d, ex0 + 14, py + 14, 'AGENT PROPOSES A CHANGE', PURPLE, 13)
    text(d, (ex0 + 18, py + 58), 'Summary: three points from the article that', 19)
    text(d, (ex0 + 18, py + 86), 'match your notes, with links to the source.', 19)
    pill(d, ex0 + 18, py + 122, 'Apply', GREEN, 15)
    pill(d, ex0 + 110, py + 122, 'Reject', '#EEF0E9', 15)
    text(d, (ex0 + 220, py + 128), 'Nothing changes without you.', 16, MUTED)

    # Foundation
    box(d, (64, 862, 1536, 948), INK, 22)
    text(d, (94, 878), 'ONE FOUNDATION', 18, GREEN, True)
    text(d, (94, 906), 'Chromium engine  /  Info objects  /  Native UI DSL  /  Built-in agent  /  MCP for your agent', 24, WHITE)
    text(d, (66, 966), 'CONCEPT ILLUSTRATION — NOT A PRODUCT SCREENSHOT', 15, MUTED)
    im.save(OUT / 'hero.png', optimize=True)


def architecture():
    im, d = canvas(1240)
    pill(d, 64, 38, 'PLIANT / ARCHITECTURE')
    text(d, (64, 96), 'Users shape the experience.', 56, bold=True)
    text(d, (64, 164), 'Pliant keeps the foundation dependable.', 40, MUTED)

    L, R = 64, 1080  # Pliant column; external agent on the right

    # 1. User + AI writes DSL
    text(d, (L + 4, 246), 'USER + THEIR AI', 18, MUTED, True)
    box(d, (L, 276, R, 380), GREEN, 18)
    text(d, (L + 24, 294), '1  UI customization DSL', 28, bold=True)
    text(d, (L + 24, 338), 'Browse area  /  Edit area  /  Agent area  /  Triggers and workflows', 21)
    arrow(d, ((L + R) // 2, 380), ((L + R) // 2, 418))
    text(d, ((L + R) // 2 + 14, 386), 'AppKit renderer: diff-based partial refresh', 16, MUTED)

    # Three layers
    cols = [
        ('2  Browser layer', 'Capability APIs over', 'the Pliant embedder', BLUE),
        ('3  Editor layer', 'Where the user steers', 'agents; scratch pads', ORANGE),
        ('4  Built-in agent', 'Watches activity;', 'proposes Changes', PURPLE),
    ]
    cw = (R - L - 40) // 3
    for i, (t, a, b, col) in enumerate(cols):
        x = L + i * (cw + 20)
        box(d, (x, 418, x + cw, 560), col, 18)
        text(d, (x + 20, 436), t, 25, bold=True)
        text(d, (x + 20, 482), a, 19)
        text(d, (x + 20, 512), b, 19)
    text(d, (L + 4, 572), 'Internal IPC: Mojo', 16, MUTED, True)

    # Info objects
    box(d, (L, 600, R, 700), WHITE, 18, LINE)
    text(d, (L + 24, 616), 'Information objects', 26, bold=True)
    text(d, (L + 24, 656), 'Objects / anchors / links / revertible Changes  ·  local SQLite', 19, MUTED)

    # Trusted core
    box(d, (L, 730, R, 860), INK, 22)
    text(d, (L + 28, 750), 'TRUSTED CORE', 19, GREEN, True)
    text(d, (L + 28, 784), 'Permissions, isolation, lifecycle, preview → Apply / Reject → restore', 23, WHITE, True)
    text(d, (L + 28, 822), 'Stable, versioned contracts for everything above', 19, '#D4DFD7')

    # Engine
    box(d, (L, 890, R, 980), WHITE, 18, LINE)
    text(d, (L + 24, 906), 'Pliant-owned embedder over Chromium Content', 25, bold=True)
    text(d, (L + 24, 944), 'Not CEF. Not Electron. One Chromium in the app.', 19, MUTED)

    # External agent
    ex0, ex1 = R + 120, 1536
    text(d, (ex0 + 4, 404), "USER'S OWN AGENT", 18, MUTED, True)
    box(d, (ex0, 432, ex1, 640), '#EDE7F8', 20, '#C7BCE6')
    text(d, (ex0 + 22, 452), 'External agent', 27, bold=True)
    text(d, (ex0 + 22, 498), 'Any runtime', 19)
    text(d, (ex0 + 22, 528), 'Owns memory and', 19)
    text(d, (ex0 + 22, 556), 'personal context', 19)
    text(d, (ex0 + 22, 596), 'Never imported', 17, MUTED, True)

    # MCP: external -> Pliant
    arrow(d, (ex0, 470), (R + 4, 470), INK, 3)
    pill(d, R + 30, 436, 'MCP', GREEN, 13)
    # A2A: built-in -> external (one way)
    arrow(d, (R, 530), (ex0 - 4, 530), INK, 3)
    pill(d, R + 30, 542, 'A2A', PURPLE, 13)
    text(d, (ex0 + 4, 660), 'MCP: your agent uses Pliant.', 17, MUTED)
    text(d, (ex0 + 4, 688), 'A2A: built-in agent asks', 17, MUTED)
    text(d, (ex0 + 4, 712), 'your agent. One way.', 17, MUTED)

    # Footer
    box(d, (L, 1010, 1536, 1150), WHITE, 20, LINE)
    text(d, (L + 26, 1030), 'Users never build the data layer, IPC, or stability.', 27, bold=True)
    text(d, (L + 26, 1076), 'They describe the workflow they want. Their AI builds it on Pliant APIs.', 22, MUTED)
    text(d, (L + 26, 1110), 'macOS first. Linux and Windows later.', 19, MUTED)
    text(d, (66, 1180), 'PROPOSED DESIGN — MOST OF THIS IS NOT IMPLEMENTED YET', 16, MUTED)
    im.save(OUT / 'architecture.png', optimize=True)


if __name__ == '__main__':
    architecture()
    print('Rendered assets/architecture.png. hero.png comes from assets/workbench-hero.html (headless Chrome, 1600x810).')
