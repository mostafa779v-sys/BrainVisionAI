import torch
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

def evaluate(model, test_loader, device, class_names):

    model.eval()

    y_true = []
    y_pred = []

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())

    accuracy = accuracy_score(y_true, y_pred)

    print(f"Test Accuracy: {accuracy*100:.2f}%")

    print("\nClassification Report\n")
    print(classification_report(
        y_true,
        y_pred,
        target_names=class_names
    ))

    return confusion_matrix(y_true, y_pred)
