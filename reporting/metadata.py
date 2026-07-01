"""
====================================================
BrainVisionAI
Metadata Component
====================================================
"""

from datetime import datetime

from . import theme


class MetadataSection:

    """
    Draw report metadata.
    """

    def __init__(

        self,

        canvas,

        model_name,

        version,

        device,

        image_size

    ):

        self.canvas = canvas

        self.model_name = model_name

        self.version = version

        self.device = device

        self.image_size = image_size

    # =====================================================

    def draw_item(

        self,

        x,

        y,

        title,

        value

    ):

        self.canvas.text(

            x,

            y,

            title,

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        self.canvas.text(

            x,

            y + 35,

            value,

            theme.TEXT_FONT,

            theme.BLACK

        )

    # =====================================================

    def draw(self):

        y = 1140

        self.canvas.line(

            40,

            y - 20,

            1560,

            y - 20

        )

        self.draw_item(

            50,

            y,

            "Model",

            self.model_name

        )

        self.draw_item(

            350,

            y,

            "Version",

            self.version

        )

        self.draw_item(

            650,

            y,

            "Device",

            self.device.upper()

        )

        self.draw_item(

            900,

            y,

            "Image Size",

            f"{self.image_size} x {self.image_size}"

        )

        self.draw_item(

            1220,

            y,

            "Generated",

            datetime.now().strftime(

                "%Y-%m-%d %H:%M"

            )

        )
