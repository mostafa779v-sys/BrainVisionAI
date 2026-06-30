import torch

# Device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Image Settings
IMAGE_SIZE = 224
NUM_CLASSES = 4

# Training Settings
BATCH_SIZE = 32
LEARNING_RATE = 0.0001
EPOCHS = 10

# Dataset Classes
CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

# Dataset Paths
TRAIN_PATH = "dataset/Training"
TEST_PATH = "dataset/Testing"

# Model Save Path
MODEL_PATH = "Models/BrainVisionAI_v1.pth"
