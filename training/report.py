
"""
BrainVisionAI - report.py
Professional diagnostic report generator (v0.5 starter)
"""

import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1400
HEADER = 90
MARGIN = 40
IMG_W = 600
IMG_H = 600

def _font(size, bold=False):
    for name in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        try:
            return ImageFont.truetype(name,size)
        except:
            pass
    return ImageFont.load_default()

def _bar(draw,x,y,w,h,pct,color=(52,152,219)):
    draw.rounded_rectangle((x,y,x+w,y+h),radius=8,outline=(180,180,180),fill=(235,235,235))
    fw=int(w*max(0,min(100,pct))/100)
    if fw>0:
        draw.rounded_rectangle((x,y,x+fw,y+h),radius=8,fill=color)

def create_report(original_image_path,
                  gradcam_image_path,
                  diagnosis="Unknown",
                  confidence=0.0,
                  probabilities=None,
                  model_name="EfficientNet-B0",
                  version="BrainVisionAI v0.5",
                  save_path="../results/report.png"):

    if probabilities is None:
        probabilities={}

    os.makedirs(os.path.dirname(save_path),exist_ok=True)

    orig=Image.open(original_image_path).convert("RGB").resize((IMG_W,IMG_H))
    grad=Image.open(gradcam_image_path).convert("RGB").resize((IMG_W,IMG_H))

    report=Image.new("RGB",(WIDTH,1100),"white")
    d=ImageDraw.Draw(report)

    title=_font(42,True)
    h1=_font(26,True)
    txt=_font(22)

    d.rectangle((0,0,WIDTH,HEADER),fill=(30,60,120))
    d.text((30,22),"BrainVisionAI",font=title,fill="white")
    d.text((980,32),"AI Diagnostic Report",font=h1,fill="white")

    report.paste(orig,(50,120))
    report.paste(grad,(750,120))

    d.text((230,735),"Original MRI",font=h1,fill="black")
    d.text((955,735),"Grad-CAM",font=h1,fill="black")

    y=790
    d.text((50,y),"Diagnosis:",font=h1,fill="black")
    d.text((220,y),diagnosis.upper(),font=h1,fill=(180,0,0))

    y+=45
    d.text((50,y),f"Confidence: {confidence:.2f}%",font=txt,fill="black")

    y+=70
    d.text((50,y),"Class Probabilities",font=h1,fill="black")
    y+=45

    for cls,val in probabilities.items():
        d.text((50,y),cls,font=txt,fill="black")
        _bar(d,240,y+4,500,22,val)
        d.text((760,y),f"{val:.2f}%",font=txt,fill="black")
        y+=42

    d.line((40,1010,1360,1010),fill=(180,180,180),width=2)
    d.text((50,1030),f"Model: {model_name}",font=txt,fill="gray")
    d.text((430,1030),f"Version: {version}",font=txt,fill="gray")
    d.text((860,1030),datetime.now().strftime("Generated: %Y-%m-%d %H:%M"),font=txt,fill="gray")

    report.save(save_path)
    print("Report saved:",save_path)
    return save_path
