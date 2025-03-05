# Voice Controlled Robotic Arm

This project implements a voice-controlled robotic arm using Arduino and Python. The robotic arm can be controlled by voice commands to rotate servos to specific angles on designated pins.

## Features

- **Voice Control**: Use voice commands to specify the pin and angle for servo rotation.
- **Arduino Integration**: Controls servos connected to an Arduino board.
- **Text-to-Speech Feedback**: Provides audio feedback using the `pyttsx3` library.
- **Speech Recognition**: Utilizes the `speech_recognition` library to interpret voice commands.

## Components

- Arduino board (e.g., Arduino Uno)
- Servo motors
- Microphone for voice input
- Python libraries: `pyfirmata`, `pyttsx3`, `speech_recognition`, `word2number`

## Setup

1. **Hardware Setup**:
   - Connect the servos to the Arduino pins as follows:
     - Base: Pin 9
     - Shoulder: Pin 10
     - Elbow: Pin 11
     - Wrist: Pin 12
     - Grip: Pin 13
   - Connect the Arduino to your computer via USB.
  
2.  **Requirements**:
  - Python 3.x
  - `pyfirmata` library for Arduino communication
  - `pyttsx3` library for text-to-speech functionality
  - `speech_recognition` library for voice command processing
  - `word2number` library for converting spoken numbers to integers
  - Arduino board with connected servo motors

3. **Software Setup**:
   - Install the required Python libraries:
     ```bash
     pip install pyfirmata pyttsx3 speechrecognition word2number
     ```
   - Upload the StandardFirmata sketch to your Arduino board using the Arduino IDE.

4. **Running the Project**:
   - Run the Python script:
     ```bash
     python robotic_arm.py
     ```
   - Follow the voice prompts to control the robotic arm.
