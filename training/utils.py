import os
import torch
from PIL import Image


def save_model(model, path):
    """
    Save model weights.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(model.state_dict(), path)
    print(f"✅ Model saved: {path}")


def load_model_weights(model, path, device):
    """
    Load trained model weights.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found: {path}")

    state_dict = torch.load(path, map_location=device)
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()

    print(f"✅ Model loaded: {path}")

    return model


def load_image(image_path):
    """
    Load RGB image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path).convert("RGB")
    return image


def print_success(message):
    print(f"✅ {message}")


def print_error(message):
    print(f"❌ {message}")


def print_line():
    print("=" * 50)
