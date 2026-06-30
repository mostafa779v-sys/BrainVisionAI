from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from config import *

# =========================
# Data Transforms
# =========================

train_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
])

test_transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])

# =========================
# Datasets
# =========================

train_dataset = datasets.ImageFolder(
    TRAIN_PATH,
    transform=train_transform
)

test_dataset = datasets.ImageFolder(
    TEST_PATH,
    transform=test_transform
)

# =========================
# Data Loaders
# =========================

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)
