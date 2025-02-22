import cv2
from ultralytics import YOLO
import os

model = YOLO("yolo11s.pt")  
model.cpu()

image_folder = "D:\\CV\\images\\"

for img_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_name)
    
    # Read the image
    img = cv2.imread(img_path)
    
    # Run YOLO detection
    results = model(img)
    
    # Check if a person is detected
    has_person = any(
    (det.boxes.cls.cpu().numpy() == 0).any()
    for det in results
    )

    
    if not has_person:
        os.remove(img_path)  # Delete the image
        print(f"Deleted {img_name} (No players detected)")

print("Filtering complete!")
