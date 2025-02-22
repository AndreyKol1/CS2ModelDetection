if __name__ == '__main__':
    from ultralytics import YOLO

    model = YOLO("yolo11s.pt")
    result = model.train(data="config.yaml", epochs=50, patience=10, batch=16, device="cuda", workers=4)
