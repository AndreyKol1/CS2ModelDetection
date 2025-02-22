import os 

img_dir = "D:\\CV\\images\\"



with open("train.txt", "r") as f:
    data = list(line.split('/')[2].strip() for line in f)

for file in os.listdir(img_dir):
    if file not in data:
        os.remove(f"D:\\CV\\images\\{file}")

