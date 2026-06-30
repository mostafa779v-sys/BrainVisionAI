from PIL import Image
import torch
import torch.nn.functional as F


def predict_image(model, image_path, transform, device, class_names):

    image = Image.open(image_path).convert("RGB")

    image = transform(image).unsqueeze(0).to(device)

    model.eval()

    with torch.no_grad():

        output = model(image)

        probabilities = F.softmax(output, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()

    confidence = probabilities[0][prediction].item() * 100

    return class_names[prediction], confidence
