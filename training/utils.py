import torch


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


def print_line():

    print("=" * 50)


def print_success(message):

    print(f"✅ {message}")


def print_error(message):

    print(f"❌ {message}")
