"""
=========================================
BrainVisionAI
Theme
=========================================
"""

from PIL import ImageFont

# ==========================================
# Page
# ==========================================

PAGE_WIDTH = 1600
PAGE_HEIGHT = 1200

# ==========================================
# Colors
# ==========================================

BACKGROUND = (246,248,252)

WHITE = (255,255,255)

BLACK = (35,35,35)

GRAY = (120,120,120)

LIGHT_GRAY = (225,225,225)

PRIMARY = (33,73,140)

SUCCESS = (46,204,113)

WARNING = (241,196,15)

DANGER = (231,76,60)

# ==========================================
# Fonts
# ==========================================

def font(size,bold=False):

    if bold:
        names=[
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "DejaVuSans-Bold.ttf"
        ]
    else:
        names=[
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "DejaVuSans.ttf"
        ]

    for n in names:
        try:
            return ImageFont.truetype(n,size)
        except:
            pass

    return ImageFont.load_default()


TITLE_FONT = font(40,True)

HEADER_FONT = font(28,True)

TEXT_FONT = font(22)

SMALL_FONT = font(18)

BIG_FONT = font(34,True)
