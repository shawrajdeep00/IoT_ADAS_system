# IoT_ADAS_system



## Drowsiness and Yawning Detection System

### Overview
The Python script implements a drowsiness and yawning detection system in a raspberry pi board using facial landmarks and computer vision techniques. It analyzes eye aspect ratio (EAR) and lip distance to determine if a person is drowsy or yawning, providing real-time alerts.

### Features
- **Real-time Detection**: The system operates in real-time, monitoring the user's facial expressions continuously.
- **Facial Landmark Detection**: Utilizes dlib for accurate facial landmark detection, enabling precise analysis of eye and lip movements.
- **EAR Calculation**: Calculates the eye aspect ratio (EAR) to detect drowsiness based on eye closure patterns.
- **Lip Distance Measurement**: Measures lip distance to identify yawning, a common sign of drowsiness.
- **Alert System**: Issues alerts when drowsiness or yawning is detected, prompting the user to take necessary actions.


### Requirements
- Raspberry Pi 5 MP camera module
- Python 3.x
- scipy
- imutils
- dlib
- OpenCV

### Usage Tips
- Adjust the `EYE_AR_THRESH` and `YAWN_THRESH` constants in the script for sensitivity tuning.
- For optimal performance, run the script on a system with sufficient processing power and camera resolution.

### Usage
- **dlib**: Library for facial landmark detection.
- **OpenCV**: Used for image processing and video capture.
- **imutils**: Provides convenient functions for working with OpenCV and dlib.

### Disclaimer
This system is intended for educational and demonstrative purposes. It should not be used as a substitute for professional medical or safety equipment. Use responsibly and ensure proper attention is given to safety while operating vehicles or machinery.

