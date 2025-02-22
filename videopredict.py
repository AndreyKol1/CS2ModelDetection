
import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")  

video_path = "cs2vid.mp4"
cap = cv2.VideoCapture(video_path)


fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*"mp4v")  
out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height))


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  


    results = model(frame)

    annotated_frame = results[0].plot()


    out.write(annotated_frame)


    cv2.imshow("YOLO Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Processing complete. Saved as 'output_video.mp4'")
