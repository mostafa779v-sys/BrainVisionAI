import os
from PIL import Image


def create_report(
    original_image_path,
    gradcam_image_path,
    save_path="../results/report.png"
):
    """
    Create a simple report that contains:
    - Original MRI
    - Grad-CAM Result
    """

    original = Image.open(original_image_path).convert("RGB")
    gradcam = Image.open(gradcam_image_path).convert("RGB")

    width = 500
    height = 500

    original = original.resize((width, height))
    gradcam = gradcam.resize((width, height))

    report = Image.new(
        "RGB",
        (width * 2, height),
        color="white"
    )

    report.paste(original, (0, 0))
    report.paste(gradcam, (width, 0))

    os.makedirs(
        os.path.dirname(save_path),
        exist_ok=True
    )

    report.save(save_path)

    return save_path
