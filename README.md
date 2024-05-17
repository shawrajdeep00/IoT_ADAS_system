# IoT_ADAS_system



## Motor and Tachometer Control on Raspberry Pi

This repository contains code for controlling a motor and reading tachometer data using Raspberry Pi and GPIO pins. The code is organized into classes to manage motor control and tachometer reading functionalities efficiently.

### Prerequisites

- Python 3.x
- RPi.GPIO library

### Installation

1. Clone this repository to your Raspberry Pi.
2. Ensure that Python 3.x and the RPi.GPIO library are installed on your system.

### Usage

1. Connect your motor to GPIO pin 4 and your tachometer sensor to GPIO pin 21 (adjust pin numbers in the code if needed).
2. Run the `main.py` script using Python.

### Code Overview

#### `motordriver` Class
- The `motordriver` class is a threaded class responsible for controlling the motor using Pulse Width Modulation (PWM).
- It initializes PWM on GPIO pin 4, sets the motor speed, and continuously adjusts the duty cycle to vary the motor's speed.

#### `tachometer` Class
- The `tachometer` class is another threaded class designed to read RPM data from the tachometer sensor.
- It sets up an event detector on GPIO pin 21 to capture rising edges, calculates RPM based on time intervals between rising edges, and computes the speed of the vehicle in meters per minute.

#### `setup()` Function
- The `setup()` function initializes the GPIO pins, sets the GPIO mode, and configures the necessary pins for motor control and tachometer reading.

#### `destroy()` Function
- The `destroy()` function is responsible for cleaning up GPIO resources when the program exits, ensuring proper resource management and preventing potential conflicts.

### Running the Program

1. Run `python main.py` in your terminal.
2. The motor will start rotating, and the program will display the speed calculated from tachometer readings.

### Notes

- Adjust the GPIO pin numbers in the code to match your hardware setup.
- Ensure proper wiring and connections before running the program.



-------------------------------------------------------------------------------------------------


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

