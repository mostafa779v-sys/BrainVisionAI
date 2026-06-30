import torch
import torch.nn as nn
import torch.optim as optim

from config import *
from model import create_model
from dataset import train_loader, test_loader

model = create_model().to(DEVICE)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

print("BrainVisionAI Training Ready")
