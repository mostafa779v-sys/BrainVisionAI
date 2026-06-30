import torch
import torch.nn.functional as F
from torchvision import transforms

from config import IMAGE_SIZE, DEVICE, CLASS_NAMES
from utils import load_image


# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])


def predict_image(model, image_path):
    """
    Predict MRI image class.

    Returns:
        prediction (str)
        confidence (float)
        probabilities (dict)
    """

    image = load_image(image_path)

    image = transform(image)

    image = image.unsqueeze(0).to(DEVICE)

    model.eval()

    with torch.no_grad():

        output = model(image)

        probs = F.softmax(output, dim=1)[0]

    confidence, prediction = torch.max(probs, 0)

    prediction_name = CLASS_NAMES[prediction.item()]

    probability_dict = {}

    for i, class_name in enumerate(CLASS_NAMES):

        probability_dict[class_name] = probs[i].item() * 100

    return (
        prediction_name,
        confidence.item() * 100,
        probability_dict
    )
