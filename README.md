# CS2ModelDetection
CS2ModelDetection is a project aimed at detecting models in Counter-Strike 2 (CS2) using a custom YOLO11 model. The system captures live gameplay(recorded videos and photos as well), processes the frames in real time with YOLO11, and overlays bounding boxes and labels onto detected models. This project demonstrates real-time object detection in a gaming environment.

<toc>
    <section id="1" title="Introduction">
        <subsection id="1.1" title="Project Overview"/>
        <subsection id="1.2" title="Features"/>
    </section>
    <section id="2" title="Installation">
        <subsection id="2.1" title="Requirements"/>
        <subsection id="2.2" title="Setup"/>
    </section>

# Overview

CS2ModelDetection is object detection algorithm, which detects T or CT(terrorists/counter-terrorists) in CS2. Built on the YOLO11 framework, the project is designed for:

1.Real-time detection with good accuracy.
2.Visualization of detection results by drawing bounding boxes with distinct colors for different classes.
3.Recording gameplay footage with annotated detections.
4.For fun and knowledge

# Features

1.Real-Time Detection: Uses a live screen capture to process CS2 gameplay.
2.Custom YOLO11 Model: Trained to detect specific classes (CT and T) with high precision.
3.Customizable Visualization: Different bounding box colors and labels for each class.

# Demo 
Watch a demo of the model in action on YouTube:
https://youtu.be/LE756txM0Q0

# Installation 
## Prerequisites

1. Pyhton 3.9 or higher
2. A CUDA-enabled GPU (optional, for faster inference)
3. CS2 installed and running (for live screen capture)

# Dependencies 
Install necessary packages using pip:
pip install opencv-python mss pygetwindow ultralytics numpy

# Usage
1. Detection on image: place your image with name 1.jpg in a folder with a imagePredidction.py and run python file(if you don't have IDE), otherwise you can change name and path
2. Detection on recorded video: place your video with name cs2vid.mp4 in a folder with a videoPrediction.py and run python file(if you don't have IDE), otherwise you can change name and path
3. Live prediction: you need to open cs2 firstly and afterwards run the script livePredcit.py.











