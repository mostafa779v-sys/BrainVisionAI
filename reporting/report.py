"""
====================================================
BrainVisionAI
Report Interface
====================================================
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

    version="v0.5",

    device="cpu",

    image_size=224

):

    """
    Generate BrainVisionAI Report.

    Returns
    -------
    output_path
    """

    builder = ReportBuilder(

        original_image=original_image,

        gradcam_image=gradcam_image,

        diagnosis=diagnosis,

        confidence=confidence,

        probabilities=probabilities,

        model_name=model_name,

        version=version,

        device=device,

        image_size=image_size

    )

    builder.save(

        output_path

    )

    return output_path
