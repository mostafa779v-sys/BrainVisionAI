"""
====================================================
BrainVisionAI
Canvas Engine
====================================================
"""

import os

from PIL import (

    Image,

    ImageDraw

)

from . import theme


class ReportCanvas:

    def __init__(self):

        self.image = Image.new(

            "RGB",

            (

                theme.PAGE_WIDTH,

                theme.PAGE_HEIGHT

            ),

            theme.BACKGROUND

        )

        self.draw = ImageDraw.Draw(

            self.image

        )

    # ======================================

    def save(

        self,

        path

    ):

        os.makedirs(

            os.path.dirname(path),

            exist_ok=True

        )

        self.image.save(path)

    # ======================================

    def line(

        self,

        x1,

        y1,

        x2,

        y2,

        color=theme.BORDER,

        width=2

    ):

        self.draw.line(

            (

                x1,

                y1,

                x2,

                y2

            ),

            fill=color,

            width=width

        )

    # ======================================

    def text(

        self,

        x,

        y,

        value,

        font,

        color=theme.BLACK

    ):

        self.draw.text(

            (

                x,

                y

            ),

            str(value),

            fill=color,

            font=font

        )

    # ======================================

    def rounded_box(

        self,

        x,

        y,

        w,

        h,

        fill=theme.CARD,

        outline=theme.BORDER

    ):

        self.draw.rounded_rectangle(

            (

                x,

                y,

                x+w,

                y+h

            ),

            radius=theme.CARD_RADIUS,

            fill=fill,

            outline=outline,

            width=theme.CARD_BORDER

        )

    # ======================================

    def rectangle(

        self,

        x,

        y,

        w,

        h,

        color

    ):

        self.draw.rectangle(

            (

                x,

                y,

                x+w,

                y+h

            ),

            fill=color

        )

    # ======================================

    def paste_image(

        self,

        image,

        x,

        y,

        w,

        h

    ):

        image = image.resize(

            (

                w,

                h

            )

        )

        self.image.paste(

            image,

            (

                x,

                y

            )

        )

    # ======================================

    def shadow_box(

        self,

        x,

        y,

        w,

        h

    ):

        self.draw.rounded_rectangle(

            (

                x+4,

                y+4,

                x+w+4,

                y+h+4

            ),

            radius=theme.CARD_RADIUS,

            fill=(220,220,220)

        )

        self.rounded_box(

            x,

            y,

            w,

            h

        )
