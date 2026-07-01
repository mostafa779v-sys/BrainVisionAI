"""
====================================================
BrainVisionAI
Reporting Theme
====================================================
"""

from PIL import ImageFont

# ==================================================
# Colors
# ==================================================

WHITE = (255, 255, 255)

BLACK = (20, 20, 20)

LIGHT_GRAY = (240, 240, 240)

GRAY = (170, 170, 170)

DARK_GRAY = (70, 70, 70)

PRIMARY = (24, 73, 125)

SECONDARY = (52, 152, 219)

SUCCESS = (39, 174, 96)

WARNING = (243, 156, 18)

DANGER = (192, 57, 43)

BORDER = (220, 220, 220)

BACKGROUND = (248, 249, 252)

CARD = (255, 255, 255)

# ==================================================
# Report Size
# ==================================================

PAGE_WIDTH = 1600

PAGE_HEIGHT = 1250

HEADER_HEIGHT = 120

FOOTER_HEIGHT = 60

MARGIN = 40

CARD_RADIUS = 20

CARD_BORDER = 2

# ==================================================
# Image Panels
# ==================================================

IMAGE_WIDTH = 650

IMAGE_HEIGHT = 650

IMAGE_PADDING = 10

# ==================================================
# Fonts
# ==================================================

def load_font(size, bold=False):

    paths = [

        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",

        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",

        "arialbd.ttf",

        "arial.ttf"

    ]

    if not bold:

        paths = [

            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",

            "arial.ttf",

            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

        ]

    for path in paths:

        try:

            return ImageFont.truetype(path, size)

        except:

            pass

    return ImageFont.load_default()

TITLE_FONT = load_font(42, True)

HEADER_FONT = load_font(28, True)

SECTION_FONT = load_font(22, True)

TEXT_FONT = load_font(20)

SMALL_FONT = load_font(16)

BIG_FONT = load_font(36, True)

PERCENT_FONT = load_font(30, True)
