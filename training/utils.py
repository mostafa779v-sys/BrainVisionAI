import torch
from PIL import Image


def save_model(model, path):

    torch.save(model.state_dict(), path)

    print(f"\n✅ Model saved to: {path}")


def load_model_weights(model, path, device):

    model.load_state_dict(
        torch.load(path, map_location=device)
    )

    model.to(device)

    model.eval()

    print(f"\n✅ Model loaded from: {path}")

    return model


def load_image(image_path):

    try:

        image = Image.open(image_path).convert("RGB")

        print("✅ Image Loaded Successfully")

        return image

    except Exception as e:

        print(f"❌ Error: {e}")

        return None


def print_line():

    print("=" * 50)


def print_success(message):

    print(f"✅ {message}")


def print_error(message):

    print(f"❌ {message}")
