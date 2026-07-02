"""
====================================================
BrainVisionAI
Professional Report Builder
====================================================
"""

from .canvas import ReportCanvas

from .header import Header
from .footer import Footer
from .images import MRISection
from .cards import DiagnosisCard
from .charts import ProbabilityChart
from .metadata import MetadataSection


class ReportBuilder:

    """
    Professional Report Builder
    """

    def __init__(

        self,

        original_image,

        gradcam_image,

        diagnosis,

        confidence,

        probabilities,

        model_name,

        version,

        device,

        image_size

    ):

        self.canvas = ReportCanvas()

        self.original_image = original_image
        self.gradcam_image = gradcam_image

        self.diagnosis = diagnosis
        self.confidence = confidence
        self.probabilities = probabilities

        self.model_name = model_name
        self.version = version
        self.device = device
        self.image_size = image_size

    # =====================================================

    def build(self):

        # ------------------------------------------
        # Header
        # ------------------------------------------

        Header(

            self.canvas,

            self.version

        ).draw()

        # ------------------------------------------
        # MRI Images
        # ------------------------------------------

        MRISection(

            self.canvas,

            self.original_image,

            self.gradcam_image

        ).draw()

        # ------------------------------------------
        # Diagnosis Card
        # ------------------------------------------

        DiagnosisCard(

            self.canvas,

            self.diagnosis,

            self.confidence

        ).draw()

        # ------------------------------------------
        # Probability Chart
        # ------------------------------------------

        ProbabilityChart(

            self.canvas,

            self.probabilities

        ).draw()

        # ------------------------------------------
        # Metadata
        # ------------------------------------------

        MetadataSection(

            self.canvas,

            self.model_name,

            self.version,

            self.device,

            self.image_size

        ).draw()

        # ------------------------------------------
        # Footer
        # ------------------------------------------

        Footer(

            self.canvas,

            self.model_name

        ).draw()

        return self.canvas

    # =====================================================

    def save(

        self,

        output_path

    ):

        canvas = self.build()

        canvas.save(

            output_path

        )

        return output_path
