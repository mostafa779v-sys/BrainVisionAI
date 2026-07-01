import os
import torch
from PIL import Image


# ==========================================
# Save Model
# ==========================================

def save_model(model, path):
    """
    Save trained model weights.
    """

    os.makedirs(os.path.dirname(path), exist_ok=True)

    torch.save(model.state_dict(), path)

    size = os.path.getsize(path) / (1024 * 1024)

    print("\n==========================================")
    print("✅ Model Saved Successfully")
    print(f"📁 Path : {path}")
    print(f"📦 Size : {size:.2f} MB")
    print("==========================================\n")


# ==========================================
# Load Model
# ==========================================

def load_model_weights(model, path, device):
    """
    Load trained model weights.
    """

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model not found:\n{path}"
        )

    state_dict = torch.load(
        path,
        map_location=device
    )

    model.load_state_dict(state_dict)

    model.to(device)

    model.eval()

    print("✅ Model Loaded Successfully")

    return model


# ==========================================
# Load Image
# ==========================================

def load_image(image_path):
    """
    Load MRI image.
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found:\n{image_path}"
        )

    image = Image.open(image_path).convert("RGB")

    return image


# ==========================================
# Console Messages
# ==========================================

def print_success(message):
    print(f"✅ {message}")


def print_error(message):
    print(f"❌ {message}")


def print_warning(message):
    print(f"⚠️ {message}")


def print_line():
    print("=" * 50)
