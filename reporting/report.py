"""
=========================================
BrainVisionAI
Report API
=========================================
"""

from .builder import ReportBuilder


def create_report(

    original_image,

    gradcam_image,

    diagnosis,

    confidence,

    probabilities,

    output_path="../results/BrainVisionAI_Report.jpg",

    model_name="EfficientNet-B0",

    version="v1.0",

    device="cuda",

    image_size=224

):

    builder = ReportBuilder(

        original_image,

        gradcam_image,

        diagnosis,

        confidence,

        probabilities,

        model_name,

        version,

        device,

        image_size

    )

    return builder.save(output_path)
