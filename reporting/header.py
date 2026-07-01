"""
====================================================
BrainVisionAI
Header Component
====================================================
"""

from . import theme


class Header:

    def __init__(

        self,

        canvas,

        version="v0.5"

    ):

        self.canvas = canvas

        self.version = version

    def draw(self):

        self.canvas.rectangle(

            0,

            0,

            theme.PAGE_WIDTH,

            theme.HEADER_HEIGHT,

            theme.PRIMARY

        )

        self.canvas.text(

            35,

            28,

            "🧠 BrainVisionAI",

            theme.TITLE_FONT,

            theme.WHITE

        )

        self.canvas.text(

            1180,

            35,

            "AI Diagnostic Report",

            theme.SECTION_FONT,

            theme.WHITE

        )

        self.canvas.text(

            1180,

            70,

            f"Version : {self.version}",

            theme.SMALL_FONT,

            theme.WHITE

        )

        self.canvas.line(

            0,

            theme.HEADER_HEIGHT,

            theme.PAGE_WIDTH,

            theme.HEADER_HEIGHT,

            theme.SECONDARY,

            3

        )
