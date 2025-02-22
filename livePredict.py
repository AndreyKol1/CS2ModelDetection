import cv2
import numpy as np
import mss
import pygetwindow as gw
from ultralytics import YOLO


model = YOLO("runs/detect/train/weights/best.pt")


class_labels = {1: "CT", 0: "T"}
class_colors = {1: (255, 0, 0), 0: (0, 0, 255)}  


def get_game_window(title="Counter-Strike 2"):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        game_win = windows[0]
        return game_win.left, game_win.top, game_win.width, game_win.height
    return None


game_window = get_game_window("Counter-Strike 2")
if not game_window:
    print("Game window not found! Make sure CS2 is running.")
    exit()


left, top, width, height = game_window
monitor = {"top": top, "left": left, "width": width, "height": height}

sct = mss.mss()

while True:

    screenshot = sct.grab(monitor)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)


    results = model(frame)


    detections = results[0].boxes

    if detections is not None:
        for box in detections:
            coords = box.xyxy[0].cpu().numpy().astype(int)
            x1, y1, x2, y2 = coords


            conf = box.conf.cpu().numpy()[0]
            class_id = int(box.cls.cpu().numpy()[0])
            label_text = class_labels.get(class_id, "Unknown")
            label = f"{label_text}: {conf:.2f}"

            color = class_colors.get(class_id, (0, 255, 0))  


            cv2.rectangle(frame, (x1, y1), (x2, y2), color=color, thickness=2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("CS2 Player Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
