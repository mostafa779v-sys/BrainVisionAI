"""
====================================================
BrainVisionAI
Cards Components
====================================================
"""

from . import theme


# =====================================================
# Base Card
# =====================================================

class Card:

    def __init__(

        self,

        canvas,

        x,

        y,

        width,

        height,

        title

    ):

        self.canvas = canvas

        self.x = x

        self.y = y

        self.width = width

        self.height = height

        self.title = title

    # ============================================

    def draw_background(self):

        self.canvas.shadow_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        self.canvas.text(

            self.x + 25,

            self.y + 20,

            self.title,

            theme.HEADER_FONT,

            theme.PRIMARY

        )


# =====================================================
# Diagnosis Card
# =====================================================

class DiagnosisCard(Card):

    def __init__(

        self,

        canvas,

        diagnosis,

        confidence,

        x=50,

        y=880,

        width=720,

        height=250

    ):

        super().__init__(

            canvas,

            x,

            y,

            width,

            height,

            "Diagnosis"

        )

        self.diagnosis = diagnosis

        self.confidence = confidence

    # ============================================

    def _diagnosis_color(self):

        diagnosis = self.diagnosis.lower()

        if diagnosis == "notumor":

            return theme.SUCCESS

        return theme.DANGER

    # ============================================

    def draw(self):

        self.draw_background()

        self.canvas.text(

            self.x + 30,

            self.y + 85,

            self.diagnosis.upper(),

            theme.BIG_FONT,

            self._diagnosis_color()

        )

        self.canvas.text(

            self.x + 30,

            self.y + 150,

            "Model Confidence",

            theme.TEXT_FONT,

            theme.DARK_GRAY

        )

        self.canvas.text(

            self.x + 320,

            self.y + 145,

            f"{self.confidence:.2f}%",

            theme.PERCENT_FONT,

            theme.PRIMARY
        )

        self.canvas.line(

            self.x + 25,

            self.y + 195,

            self.x + self.width - 25,

            self.y + 195

        )

        if self.confidence >= 95:

            status = "Very High Confidence"

            color = theme.SUCCESS

        elif self.confidence >= 85:

            status = "High Confidence"

            color = theme.SECONDARY

        elif self.confidence >= 70:

            status = "Moderate Confidence"

            color = theme.WARNING

        else:

            status = "Low Confidence"

            color = theme.DANGER

        self.canvas.text(

            self.x + 30,

            self.y + 210,

            status,

            theme.TEXT_FONT,

            color

        )


# =====================================================
# Confidence Card
# =====================================================

class ConfidenceCard(Card):

    def __init__(

        self,

        canvas,

        confidence,

        x,

        y,

        width=250,

        height=170

    ):

        super().__init__(

            canvas,

            x,

            y,

            width,

            height,

            "Confidence"

        )

        self.confidence = confidence

    # ============================================

    def draw(self):

        self.draw_background()

        self.canvas.text(

            self.x + 45,

            self.y + 70,

            f"{self.confidence:.2f}%",

            theme.BIG_FONT,

            theme.PRIMARY

        )


# =====================================================
# Information Card
# =====================================================

class InfoCard(Card):

    def __init__(

        self,

        canvas,

        title,

        value,

        x,

        y,

        width=250,

        height=170

    ):

        super().__init__(

            canvas,

            x,

            y,

            width,

            height,

            title

        )

        self.value = value

    # ============================================

    def draw(self):

        self.draw_background()

        self.canvas.text(

            self.x + 30,

            self.y + 75,

            str(self.value),

            theme.SECTION_FONT,

            theme.BLACK

        )
