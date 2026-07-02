"""
=========================================
BrainVisionAI
Canvas
=========================================
"""

import os

from PIL import Image
from PIL import ImageDraw

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

    def save(self, path):

        folder = os.path.dirname(path)

        if folder:

            os.makedirs(

                folder,

                exist_ok=True

            )

        self.image.save(

            path,

            quality=100

        )

    # ======================================

    def text(

        self,

        x,

        y,

        text,

        font,

        color=theme.BLACK

    ):

        self.draw.text(

            (

                x,

                y

            ),

            str(text),

            fill=color,

            font=font

        )

    # ======================================

    def line(

        self,

        x1,

        y1,

        x2,

        y2,

        color=theme.LIGHT_GRAY,

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

    def box(

        self,

        x,

        y,

        w,

        h,

        fill=theme.WHITE,

        outline=theme.LIGHT_GRAY,

        radius=20

    ):

        self.draw.rounded_rectangle(

            (

                x,

                y,

                x+w,

                y+h

            ),

            radius=radius,

            fill=fill,

            outline=outline,

            width=2

        )

    # ======================================

    def image_box(

        self,

        path,

        x,

        y,

        w,

        h

    ):

        img = Image.open(path).convert("RGB")

        img.thumbnail(

            (

                w-20,

                h-20

            )

        )

        ox = (

            w -

            img.width

        ) // 2

        oy = (

            h -

            img.height

        ) // 2

        self.box(

            x,

            y,

            w,

            h

        )

        self.image.paste(

            img,

            (

                x+ox,

                y+oy

            )

        )

    # ======================================

    def progress(

        self,

        x,

        y,

        w,

        value,

        color

    ):

        self.draw.rounded_rectangle(

            (

                x,

                y,

                x+w,

                y+22

            ),

            radius=11,

            fill=(235,235,235)

        )

        filled = int(

            w *

            value /

            100

        )

        self.draw.rounded_rectangle(

            (

                x,

                y,

                x+filled,

                y+22

            ),

            radius=11,

            fill=color

        )
