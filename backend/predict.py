import torch
import torchvision.models as models
from PIL import Image
from torchvision.models import ResNet34_Weights


def predict(eyePic: Image):
    weights = ResNet34_Weights.DEFAULT

    # 1. Map class labels alphabetically matching ImageFolder order
    class_names = ['Conjunctivitis', 'Normal', 'Uveitis']

    # 2. Re-instantiate model architecture & match output classes
    device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    model = models.resnet34()
    model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))

    # 3. Load saved state dict & set to evaluation mode
    model.load_state_dict(torch.load('../app/checkpoints/resnet34_eye_disease.pt', map_location=device))
    model.to(device)
    model.eval()

    # 4. Load image, apply transformations, and add batch dimension
    transform = weights.transforms()
    input_tensor = transform(eyePic).unsqueeze(0).to(device)

    # 5. Run inference without gradient computation
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        predicted_idx = torch.argmax(probabilities).item()

    # 6. Extract result and print confidence score
    predicted_label = class_names[predicted_idx]
    confidence = probabilities[predicted_idx].item() * 100

    return {
        "disease": predicted_label,
        "condidence": round(confidence, 2)
    }