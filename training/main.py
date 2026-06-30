# ==========================================
# BrainVisionAI v0.2
# Main Program
# ==========================================

from config import DEVICE, IMAGE_SIZE, CLASS_NAMES, MODEL_PATH
from model import create_model
from utils import load_model_weights, print_success, print_error
from predict import predict_image

import os


def header():

    print("=" * 50)
    print("🧠 BrainVisionAI v0.2")
    print("=" * 50)

    print(f"Device      : {DEVICE}")
    print(f"Image Size  : {IMAGE_SIZE}")
    print(f"Classes     : {len(CLASS_NAMES)}")


def load_model():

    print("\nLoading trained model...\n")

    model = create_model()

    model = load_model_weights(
        model,
        MODEL_PATH,
        DEVICE
    )

    print_success("BrainVisionAI Ready!")

    return model


def predict_menu(model):

    image_path = input("\nEnter MRI image path:\n")

    if not os.path.exists(image_path):

        print_error("Image not found!")

        return

    prediction, confidence, probabilities = predict_image(
        model,
        image_path
    )

    print("\n" + "=" * 50)

    print(f"Prediction : {prediction}")

    print(f"Confidence : {confidence:.2f}%")

    print("\nProbabilities:\n")

    for name, value in probabilities.items():

        print(f"{name:<12}: {value:.2f}%")

    print("=" * 50)


def main():

    header()

    model = load_model()

    while True:

        print("\n")

        print("1 - Train Model")
        print("2 - Evaluate Model")
        print("3 - Predict MRI")
        print("4 - Exit")

        choice = input("\nChoice: ")

        if choice == "3":

            predict_menu(model)

        elif choice == "4":

            print("\nGoodbye!")

            break

        else:

            print("\nModule will be added in next version.")


if __name__ == "__main__":

    main()
