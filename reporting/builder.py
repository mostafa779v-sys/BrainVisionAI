"""
=========================================
BrainVisionAI
Report Builder
=========================================
"""

from .canvas import ReportCanvas
from .sections import draw_report


class ReportBuilder:

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

    # =====================================

    def build(self):

        draw_report(

            self.canvas,

            self.original_image,

            self.gradcam_image,

            self.diagnosis,

            self.confidence,

            self.probabilities,

            self.model_name,

            self.version,

            self.device,

            self.image_size

        )

        return self.canvas

    # =====================================

    def save(self, output_path):

        canvas = self.build()

        canvas.save(output_path)

        return output_path
