from config import *
from model import create_model
from utils import print_success, print_error, load_image


def print_header():
    print("=" * 50)
    print("🧠 BrainVisionAI v0.1")
    print("=" * 50)


def show_system_info():
    print(f"Device      : {DEVICE}")
    print(f"Image Size  : {IMAGE_SIZE}")
    print(f"Classes     : {len(CLASS_NAMES)}")
    print()


def load_ai_model():
    print("Loading Model...")

    model = create_model().to(DEVICE)

    print_success("Model Loaded Successfully!")

    return model


def show_menu():
    print("\nChoose an option:")
    print("1 - Train Model")
    print("2 - Evaluate Model")
    print("3 - Predict MRI")
    print("4 - Exit")


def handle_choice(model):

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n🚧 Training module is under development.")

    elif choice == "2":

        print("\n🚧 Evaluation module is under development.")

    elif choice == "3":

        image_path = input("\nEnter MRI image path: ")

        image = load_image(image_path)

        if image is not None:

            print_success("Prediction module will be connected next.")

    elif choice == "4":

        print("\nGoodbye!")

    else:

        print_error("Invalid choice.")


def main():

    print_header()

    show_system_info()

    model = load_ai_model()

    show_menu()

    handle_choice(model)


if __name__ == "__main__":
    main()
