"""
====================================================
BrainVisionAI
Professional Diagnosis Card
====================================================
"""

from . import theme


class DiagnosisCard:

    """
    Professional AI Diagnosis Card
    """

    def __init__(

        self,

        canvas,

        diagnosis,

        confidence,

        x=1850,

        y=230,

        width=1250,

        height=1050

    ):

        self.canvas = canvas

        self.diagnosis = diagnosis

        self.confidence = confidence

        self.x = x

        self.y = y

        self.width = width

        self.height = height

    # =================================================

    def _color(self):

        if self.confidence >= 95:

            return theme.SUCCESS

        elif self.confidence >= 70:

            return theme.SECONDARY

        elif self.confidence >= 40:

            return theme.WARNING

        return theme.DANGER

    # =================================================

    def _reliability(self):

        if self.confidence >= 95:

            return "VERY HIGH"

        elif self.confidence >= 70:

            return "HIGH"

        elif self.confidence >= 40:

            return "MODERATE"

        return "LOW"

    # =================================================

    def draw(self):

        color = self._color()

        reliability = self._reliability()

        self.canvas.shadow_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        self.canvas.rounded_box(

            self.x,

            self.y,

            self.width,

            self.height

        )

        padding = 40

        cx = self.x + padding

        cy = self.y + padding

        # ==========================================
        # Title
        # ==========================================

        self.canvas.text(

            cx,

            cy,

            "AI Diagnosis",

            theme.HEADER_FONT,

            theme.PRIMARY

        )

        cy += 70

        # ==========================================
        # Diagnosis
        # ==========================================

        self.canvas.text(

            cx,

            cy,

            "Diagnosis",

            theme.SMALL_FONT,

            theme.GRAY

        )

        cy += 40

        self.canvas.text(

            cx,

            cy,

            self.diagnosis.upper(),

            theme.BIG_FONT,

            color

        )

        cy += 90

        # ==========================================
        # Confidence
        # ==========================================

        self.canvas.text(

            cx,

            cy,

            "Model Confidence",

            theme.SMALL_FONT,

            theme.GRAY

        )

        self.canvas.text(

            self.x + self.width - 220,

            cy,

            f"{self.confidence:.2f}%",

            theme.PERCENT_FONT,

            color

        )

        cy += 45

        self.canvas.horizontal_progress(

            cx,

            cy,

            self.width - padding * 2,

            28,

            self.confidence,

            foreground=color

        )

        cy += 70

        # ==========================================
        # Reliability
        # ==========================================

        self.canvas.text(

            cx,

            cy,

            "Prediction Reliability",

            theme.SMALL_FONT,

            theme.GRAY

        )

        self.canvas.text(

            self.x + self.width - 260,

            cy,

            reliability,

            theme.SECTION_FONT,

            color

        )

        cy += 60

        self.canvas.line(

            cx,

            cy,

            self.x + self.width - padding,

            cy,

            theme.BORDER,

            2

        )

        cy += 35        # ==========================================
        # AI Explanation
        # ==========================================

        self.canvas.text(

            cx,

            cy,

            "AI Explanation",

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        cy += 45

        explanation = (

            "The neural network detected image features "

            f"that are highly consistent with "

            f"{self.diagnosis.upper()}. "

            "The highlighted Grad-CAM region represents "

            "the image area that contributed most strongly "

            "to the final prediction."

        )

        self.canvas.text(

            cx,

            cy,

            explanation,

            theme.TEXT_FONT,

            theme.BLACK

        )

        cy += 120

        # ==========================================
        # Clinical Recommendation
        # ==========================================

        self.canvas.text(

            cx,

            cy,

            "Clinical Recommendation",

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        cy += 45

        recommendation = (

            "This AI prediction should always be reviewed "

            "together with MRI findings and interpreted by "

            "a qualified radiologist or physician."

        )

        self.canvas.text(

            cx,

            cy,

            recommendation,

            theme.TEXT_FONT,

            theme.DARK_GRAY

        )

        cy += 110

        # ==========================================
        # Summary
        # ==========================================

        self.canvas.line(

            cx,

            cy,

            self.x + self.width - 40,

            cy,

            theme.BORDER,

            2

        )

        cy += 35

        self.canvas.text(

            cx,

            cy,

            "Summary",

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        cy += 45

        summary = (

            f"The AI model classified this MRI as "

            f"{self.diagnosis.upper()} "

            f"with a confidence of "

            f"{self.confidence:.2f}%."

        )

        self.canvas.text(

            cx,

            cy,

            summary,

            theme.TEXT_FONT,

            theme.BLACK

        )

        cy += 90        # ==========================================
        # Disclaimer
        # ==========================================

        self.canvas.line(

            cx,

            cy,

            self.x + self.width - 40,

            cy,

            theme.BORDER,

            2

        )

        cy += 30

        self.canvas.text(

            cx,

            cy,

            "Disclaimer",

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        cy += 45

        disclaimer = (

            "BrainVisionAI is an AI-assisted decision "

            "support system. This report must not replace "

            "professional medical judgment."

        )

        self.canvas.text(

            cx,

            cy,

            disclaimer,

            theme.TEXT_FONT,

            theme.DARK_GRAY

        )

        cy += 100

        # ==========================================
        # Report Status
        # ==========================================

        self.canvas.line(

            cx,

            cy,

            self.x + self.width - 40,

            cy,

            theme.BORDER,

            2

        )

        cy += 30

        self.canvas.text(

            cx,

            cy,

            "Report Status",

            theme.SECTION_FONT,

            theme.PRIMARY

        )

        self.canvas.text(

            self.x + self.width - 250,

            cy,

            "COMPLETED",

            theme.SECTION_FONT,

            theme.SUCCESS

        )

        cy += 55

        self.canvas.text(

            cx,

            cy,

            "Generated automatically by BrainVisionAI.",

            theme.SMALL_FONT,

            theme.GRAY

        )
