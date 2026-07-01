import torch
import torch.nn as nn
import torch.optim as optim

from config import *
from model import create_model
from dataset import train_loader, test_loader
from utils import save_model

# ==========================
# Create Model
# ==========================

model = create_model().to(DEVICE)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

best_accuracy = 0.0

print("=" * 50)
print("🧠 BrainVisionAI Training Started")
print("=" * 50)

# ==========================
# Training Loop
# ==========================

for epoch in range(EPOCHS):

    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:

        images = images.to(DEVICE)
        labels = labels.to(DEVICE)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

    train_accuracy = 100 * correct / total

    # ==========================
    # Evaluation
    # ==========================

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(DEVICE)
            labels = labels.to(DEVICE)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)

            correct += (predicted == labels).sum().item()

    test_accuracy = 100 * correct / total

    print("-" * 50)
    print(f"Epoch {epoch+1}/{EPOCHS}")
    print(f"Loss: {running_loss/len(train_loader):.4f}")
    print(f"Train Accuracy: {train_accuracy:.2f}%")
    print(f"Test Accuracy : {test_accuracy:.2f}%")

    if test_accuracy > best_accuracy:

        best_accuracy = test_accuracy

        save_model(
            model,
            MODEL_PATH
        )

        print("✅ Best model updated.")

print("=" * 50)
print("Training Finished")
print(f"Best Test Accuracy: {best_accuracy:.2f}%")
print("=" * 50)
