import torch
from torchvision import transforms
from PIL import Image

# Paths
MODEL_PATH = "Control EfficientNet Model.pt"
IMAGE_PATH = "sample.jpg"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model (entire model was saved with torch.save(model, ...))
model = torch.load(MODEL_PATH, map_location=DEVICE)
model.eval()

# Image preprocessing (match training transforms)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load and preprocess image
img = Image.open(IMAGE_PATH).convert("RGB")
input_tensor = transform(img).unsqueeze(0).to(DEVICE)

# Predict
with torch.no_grad():
    output = model(input_tensor)
    predicted_class = torch.argmax(output, dim=1).item()

print(f"Predicted class: {predicted_class}")
