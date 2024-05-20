# IoT_ADAS_system


A MongoDB database has been developed and hosted on Atlas Cloud, containing data about geographical coordinates (latitude and longitude), congestion levels, and traffic status (represented as integers and 'GREEN'/'RED' respectively). To interact with this database, we've created several JavaScript files as part of our project.

## GPS parsing with real live traffic data in the server

1. **connection.js**

   This file establishes a connection to the MongoDB database using Mongoose. It configures the connection with the required settings such as `useNewUrlParser` and `useUnifiedTopology`. Upon successful connection, it logs a message indicating the connection success.

2. **auth.js**

   `auth.js` defines routes and middleware for handling authentication and data retrieval. It imports the database connection configuration from `connection.js` and also imports the `User` model from `userschema.js`. Notable endpoints include:
   - `/mat`: Retrieves all data from the 'map1' collection.
   - `/matl/:latn&longw`: Retrieves data based on latitude and longitude, returning traffic and signal information.

3. **userschema.js**

   This file defines the schema for the data stored in the MongoDB collection. It specifies the structure of each document, including fields such as latitude, longitude, traffic level, and signal status. The schema ensures data integrity and completeness.

4. **app.js**

   The main application file sets up an Express server, establishes a connection to the MongoDB database using `matrix` (possibly a typo for `connection.js`), and configures routes using the `auth` router. It listens on the specified port and logs a message upon server startup.

These codes collectively form a system for managing and retrieving geographic and traffic-related data from a MongoDB database using Node.js and Express.


---------------------------------------------------------------------------------------------------------------


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
2. Run the `tachometer_impl.py` script using Python.

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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Alcohol and Vibration Sensor-Based Emergency Alert Systems

### Overview
This project involves designing an emergency alert system for vehicles using alcohol and vibration sensors. The system aims to enhance road safety by monitoring the driver's alcohol consumption and detecting potential accidents, with live data sent to authorized servers for monitoring.

### Components
- **Alcohol Sensor Module**: Detects alcohol concentration in the vehicle's atmosphere, particularly around the driver's seat.
- **Buzzer**: Alerts the driver when alcohol levels are high.
- **Motor Driver**: Controls the vehicle's engine based on alcohol concentration.
- **Thingspeak Server**: Receives live data on alcohol consumption and accident alerts.
- **Vibration Sensor**: Monitors vehicle vibrations to detect accidents.
- **GPS Module**: Provides live coordinates for tracking and emergency response.


### Alcohol Detection
The system measures the alcohol concentration and responds based on predefined thresholds:

1. **Alcohol Concentration < 20%**: 
   - Engine runs normally.
   - No alerts are triggered.

2. **Alcohol Concentration 20% - 50%**: 
   - Engine runs at half speed.
   - An alert is sent to the computer display.
   - User is advised to reduce alcohol consumption.

3. **Alcohol Concentration > 50%**: 
   - Engine is completely switched off.
   - Buzzer alerts the user.
   - Data is sent to the 'traffic police server' on Thingspeak.
   - Vehicle details and GPS coordinates are reported.

#### Alcohol Level Calculation
The following Python snippet converts the analog values from the alcohol sensor into a percentage:

```python
def get_alcohol_level():
    reading = bus.read_i2c_block_data(0x50, 0x00, 2)
    reading2 = float(reading * 0.43)
    print("analog reading= ", str(reading), str(reading2), '%')
    return reading2
```

### Accident Detection
A vibration module detects excessive vibrations indicative of an accident:

1. **Normal Vibrations**:
   - Engine runs normally.
   - No alerts are triggered.

2. **Threshold Exceeded**:
   - Engine is switched off.
   - An alert is displayed on the onboard computer system.
   - Data is sent to the 'Hospitals' server on Thingspeak.
   - The hospital compares GPS coordinates to dispatch emergency services.

### Thingspeak Server
- **Alcohol Data**: Sent to 'traffic police server' with current alcohol levels and GPS coordinates.
- **Accident Data**: Sent to 'Hospitals' server with accident status and GPS coordinates.

### GPS Integration
- Write API key from Thingspeak is used.
- GPS module is parsed into the code.
- Live data visualization is achieved on the Thingspeak platform.

### Conclusion
This emergency alert system enhances vehicle safety by:
- Preventing drunk driving.
- Detecting and responding to accidents.
- Providing real-time data to authorities for timely intervention.
- Ensuring driver safety and compliance with traffic regulations.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



## AI Voice Assistant System for Convenient Driving

### Overview

This project implements an intelligent personal assistant using an artificial intelligence voice assistant system on a Raspberry Pi. The system is capable of performing multiple tasks simultaneously and managing onboard computer functionalities through hot words like "Ok Google." It handles a range of activities including speech recognition, GPS access to nearby utility stores, and retrieving information from the internet, which can be displayed on a screen. The core of this project utilizes the Google Assistant integrated with Raspberry Pi hardware via API control to facilitate two-way communication.

### Requirements

- **Hardware:**
  - Raspberry Pi
  - USB Microphone
  - USB Speaker

- **Software:**
  - Google Assistant API
  - Python 3
  - Virtual Environment
  - Required Libraries: `portaudio19-dev`, `libffi-dev`, `libssl-dev`, `google-assistant-sdk`, `google-auth-outhlib`

### Setup Instructions

#### 1. Google Assistant Console Setup

1. **Create a Project:**
   - Visit [Google Actions Console](https://console.actions.google.com/).
   - Create a new project and register your hardware as a Google Assistant device.
   - Set the device type to "speaker" and obtain the `Model ID`.

2. **OAuth Credential File:**
   - Register the model to get an OAuth credential file.
   - This file allows client applications to call the Google Assistant service.

#### 2. Enable Google Assistant API

1. **Enable API:**
   - Visit [Google API Console](https://console.developers.google.com/apis).
   - Select your project and enable the Google Assistant API.
   - Configure the consent screen and save the project.

#### 3. Configure Google Account Settings

- Enable the following in your Google account settings:
  - Web and App Activities
  - Audio and Video Recording
  - Location Services

#### 4. Hardware Connections

1. **Microphone and Speaker Setup:**
   - Identify the `card number` and `device number` for the microphone and speaker:
     ```bash
     $ arecord -l
     $ aplay -l
     ```

2. **Create `.asoundrc` File:**
   - Create and edit `.asoundrc` in the home directory:
     ```bash
     $ nano /home/pi/.asoundrc
     ```

3. **Test Audio Setup:**
   - Test the microphone and speaker:
     ```bash
     $ speaker-test -t wav
     $ arecord –format=S16_LE –duration=5 –rate=16000 –file-type=raw out.raw
     $ aplay –format=S16_LE –rate=16000 out.raw
     ```

#### 5. Software Installation

1. **Update and Upgrade:**
   - Update Raspberry Pi and install necessary packages:
     ```bash
     $ sudo apt-get update
     $ sudo apt-get upgrade
     ```

2. **Python and Virtual Environment:**
   - Install Python 3 and create a virtual environment:
     ```bash
     $ sudo apt-get install python3-dev python3-venv
     $ python3 -m venv env
     $ source env/bin/activate
     $ env/bin/python -m pip install –upgrade pip setuptools wheel
     ```

3. **Install Required Libraries:**
   - Install `libffi` and `libssl`:
     ```bash
     $ sudo apt-get install portaudio19-dev libffi-dev libssl-dev
     ```

4. **Install Google Assistant SDK:**
   - Install the SDK samples:
     ```bash
     $ python -m pip install –upgrade google-assistant-sdk[samples]
     ```

#### 6. Configure OAuth Credential

1. **Copy Credential File:**
   - Copy the OAuth credential file to `/home/pi`.

2. **Configure Shell:**
   - Configure the credential file in the shell:
     ```bash
     $ python -m pip install –upgrade google-auth-outhlib[tool]
     $ google-oauthlib-tool –scope https://www.googleapis.com/auth/assistant-sdk-prototype –save –headless –client-secrets /home/pi/[credential_file]
     ```

3. **Authorize:**
   - Google will prompt for an authorization code sent to your email.

##### 7. Test the Setup

- Verify the setup by running:
  ```bash
  $ googlesamples-assistant-pushtotalk –project-id [project_id] –device-model-id [model_id]
  ```

### Conclusion

With the setup complete, your Raspberry Pi is now an intelligent voice assistant system capable of handling various tasks and improving the driving experience with hands-free operations.
