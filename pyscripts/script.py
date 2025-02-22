import cv2

video_path = "D:\\CV\\videos\\1.mkv"  
save_dir = "D:\\CV\\images\\"  
cap = cv2.VideoCapture(video_path)  
frame_rate = 12 # Save every 5th frame  

count = 0  
while cap.isOpened():  
    ret, frame = cap.read()  
    if not ret:  
        break  
    if count % frame_rate == 0:  
        cv2.imwrite(f"{save_dir}frame_{count}_1.jpg", frame)  
    count += 1  

cap.release()  
print("Frames extracted successfully!") 
