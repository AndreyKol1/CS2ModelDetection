from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")  

results = model("3.jpg", save=True, conf=0.5)

results[0].show()
