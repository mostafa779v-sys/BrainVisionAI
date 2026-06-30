import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

from config import IMAGE_SIZE, DEVICE, CLASS_NAMES


transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])


def predict_image(model, image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0).to(DEVICE)

    model.eval()

    with torch.no_grad():

        output = model(image)

        probabilities = F.softmax(output, dim=1)

        confidence, prediction = torch.max(probabilities, 1)

    prediction = CLASS_NAMES[prediction.item()]

    confidence = confidence.item() * 100

    return prediction, confidence
