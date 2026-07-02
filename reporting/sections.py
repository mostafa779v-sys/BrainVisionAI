"""
=========================================
BrainVisionAI
Report Sections
=========================================
"""

from datetime import datetime

from . import theme
from . import layout


# =====================================================
# Header
# =====================================================

def draw_header(canvas):

    canvas.text(

        45,
        layout.HEADER_Y,

        "BrainVisionAI Diagnostic Report",

        theme.TITLE_FONT,

        theme.PRIMARY

    )

    canvas.text(

        1280,
        layout.HEADER_Y + 10,

        "AI Assisted MRI Analysis",

        theme.SMALL_FONT,

        theme.GRAY

    )

    canvas.line(

        40,

        70,

        1560,

        70

    )


# =====================================================
# MRI Images
# =====================================================

def draw_images(

    canvas,

    original_image,

    gradcam_image

):

    canvas.text(

        layout.MRI_X,

        layout.IMAGE_Y - 35,

        "Original MRI",

        theme.HEADER_FONT,

        theme.BLACK

    )

    canvas.image_box(

        original_image,

        layout.MRI_X,

        layout.IMAGE_Y,

        layout.IMAGE_W,

        layout.IMAGE_H

    )

    canvas.text(

        layout.GRADCAM_X,

        layout.IMAGE_Y - 35,

        "Grad-CAM Heatmap",

        theme.HEADER_FONT,

        theme.BLACK

    )

    canvas.image_box(

        gradcam_image,

        layout.GRADCAM_X,

        layout.IMAGE_Y,

        layout.IMAGE_W,

        layout.IMAGE_H

    )


# =====================================================
# Helpers
# =====================================================

def probability_color(value):

    if value >= 90:

        return theme.SUCCESS

    elif value >= 70:

        return theme.PRIMARY

    elif value >= 40:

        return theme.WARNING

    else:

        return theme.DANGER
      # =====================================================
# Diagnosis
# =====================================================

def draw_diagnosis(

    canvas,

    diagnosis,

    confidence

):

    canvas.box(

        layout.DIAGNOSIS_X,

        layout.DIAGNOSIS_Y,

        layout.DIAGNOSIS_W,

        layout.DIAGNOSIS_H

    )

    x = layout.DIAGNOSIS_X + 30

    y = layout.DIAGNOSIS_Y + 25

    canvas.text(

        x,

        y,

        "Diagnosis",

        theme.HEADER_FONT,

        theme.PRIMARY

    )

    y += 60

    canvas.text(

        x,

        y,

        diagnosis.upper(),

        theme.BIG_FONT,

        probability_color(confidence)

    )

    y += 70

    canvas.text(

        x,

        y,

        f"Confidence : {confidence:.2f}%",

        theme.HEADER_FONT,

        theme.BLACK

    )

    y += 60

    canvas.progress(

        x,

        y,

        600,

        confidence,

        probability_color(confidence)

    )

    y += 60

    canvas.text(

        x,

        y,

        "This prediction is generated automatically",

        theme.TEXT_FONT,

        theme.GRAY

    )

    y += 35

    canvas.text(

        x,

        y,

        "using the BrainVisionAI deep learning model.",

        theme.TEXT_FONT,

        theme.GRAY

    )


# =====================================================
# Probability
# =====================================================

def draw_probabilities(

    canvas,

    probabilities

):

    canvas.box(

        layout.PROBABILITY_X,

        layout.PROBABILITY_Y,

        layout.PROBABILITY_W,

        layout.PROBABILITY_H

    )

    x = layout.PROBABILITY_X + 30

    y = layout.PROBABILITY_Y + 25

    canvas.text(

        x,

        y,

        "Class Probabilities",

        theme.HEADER_FONT,

        theme.PRIMARY

    )

    y += 60

    for cls, value in probabilities.items():

        color = probability_color(value)

        canvas.text(

            x,

            y,

            cls,

            theme.TEXT_FONT,

            theme.BLACK

        )

        canvas.progress(

            x + 170,

            y,

            350,

            value,

            color

        )

        canvas.text(

            x + 550,

            y,

            f"{value:.2f}%",

            theme.TEXT_FONT,

            color

        )

        y += 65
      # =====================================================
# Footer
# =====================================================

def draw_footer(

    canvas,

    model_name,

    version,

    device,

    image_size

):

    y = layout.FOOTER_Y

    canvas.line(

        40,

        y - 20,

        1560,

        y - 20

    )

    canvas.text(

        50,

        y,

        f"Model : {model_name}",

        theme.SMALL_FONT,

        theme.BLACK

    )

    canvas.text(

        420,

        y,

        f"Version : {version}",

        theme.SMALL_FONT,

        theme.BLACK

    )

    canvas.text(

        700,

        y,

        f"Device : {device.upper()}",

        theme.SMALL_FONT,

        theme.BLACK

    )

    canvas.text(

        980,

        y,

        f"Image Size : {image_size} × {image_size}",

        theme.SMALL_FONT,

        theme.BLACK

    )

    canvas.text(

        1320,

        y,

        datetime.now().strftime(

            "%Y-%m-%d"

        ),

        theme.SMALL_FONT,

        theme.BLACK

    )

    canvas.text(

        50,

        y + 35,

        "Disclaimer: This report is AI-generated and should support—not replace—professional medical judgment.",

        theme.SMALL_FONT,

        theme.GRAY

    )


# =====================================================
# Main Drawing Function
# =====================================================

def draw_report(

    canvas,

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

    draw_header(

        canvas

    )

    draw_images(

        canvas,

        original_image,

        gradcam_image

    )

    draw_diagnosis(

        canvas,

        diagnosis,

        confidence

    )

    draw_probabilities(

        canvas,

        probabilities

    )

    draw_footer(

        canvas,

        model_name,

        version,

        device,

        image_size

    )
