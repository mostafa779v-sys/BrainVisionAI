# ==========================================
# BrainVisionAI v0.4
# Main Program
# ==========================================

from config import DEVICE, IMAGE_SIZE, CLASS_NAMES, MODEL_PATH
from model import create_model
from dataset import test_loader
from evaluate import evaluate
from predict import predict_image
from gradcam import generate_gradcam
from utils import (
    load_model_weights,
    print_success,
    print_error
)

import os


def header():

    print("=" * 50)
    print("🧠 BrainVisionAI v0.4")
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

    image_path = input("\nEnter MRI image path:\n").strip()

    if not os.path.exists(image_path):

        print_error("Image not found!")
        return

    prediction, confidence, probabilities = predict_image(
        model,
        image_path
    )

    print("\n" + "=" * 50)
    print("🧠 BrainVisionAI Diagnosis")
    print("=" * 50)

    print(f"\nPrediction : {prediction}")
    print(f"Confidence : {confidence:.2f}%")

    print("\nProbabilities:\n")

    for name, value in probabilities.items():
        print(f"{name:<12}: {value:.2f}%")

    print("\nGenerating Grad-CAM...\n")

    try:

        save_path = generate_gradcam(
            model,
            image_path
        )

        print_success(f"Grad-CAM saved successfully!")
        print(f"Location : {save_path}")

    except Exception as e:

        print_error(f"Grad-CAM failed:\n{e}")

    print("=" * 50)


def evaluate_menu(model):

    accuracy, _ = evaluate(
        model,
        test_loader
    )

    print(f"\n✅ Evaluation Finished")
    print(f"Final Accuracy : {accuracy*100:.2f}%")

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

        choice = input("\nChoice: ").strip()

        if choice == "1":

            print("\nRun train.py separately to train the model.")

        elif choice == "2":

            evaluate_menu(model)

        elif choice == "3":

            predict_menu(model)

        elif choice == "4":

            print("\nGoodbye!")
            break

        else:

            print_error("Invalid choice.")


if __name__ == "__main__":
    main()
