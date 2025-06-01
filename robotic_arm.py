# Import necessary libraries
from pyfirmata import Arduino, SERVO  # For Arduino board communication and controlling servo motors
from time import sleep                # To add delay between servo movements
import pyttsx3                        # Text-to-speech conversion
import speech_recognition as sr      # For voice input recognition
from word2number import w2n          # Converts spoken numbers to numerical values

# Define Arduino port and servo pin numbers
port = 'COM3'         # Change this if the Arduino is connected to a different port
base = 9              # Pin for base servo motor
shoulder = 10         # Pin for shoulder servo
elbow = 11            # Pin for elbow servo
wrist = 12            # Pin for wrist servo
grip = 13             # Pin for gripper servo

# Initialize Arduino board
board = Arduino(port)

# Set the pins connected to servos as SERVO mode
board.digital[base].mode = SERVO 
board.digital[shoulder].mode = SERVO
board.digital[elbow].mode = SERVO
board.digital[wrist].mode = SERVO
board.digital[grip].mode = SERVO

# Function to rotate a given servo to a specific angle
def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)  # Short pause to allow servo to reach the position

# Set up text-to-speech engine
engine = pyttsx3.init('sapi5')               # Using sapi5 voice engine (Windows)
voices = engine.getProperty('voices')        # Fetch available voices
engine.setProperty('voice', voices[1].id)    # Set voice (we can try voices[0] for male)

# Function to speak text out loud
def speak(audio, rate=150):
    engine.setProperty('rate', rate)  # Set speaking speed
    engine.say(audio)                 # Queue the text to speak
    engine.runAndWait()               # Play the queued speech

# Function to listen to user's voice and convert to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Wait time before assuming the user stopped talking
        audio = r.listen(source)  # Listen to audio input

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Use Google to recognize speech
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"  # Return a fallback if recognition fails
    return query

# Main program loop
if __name__ == "__main__":
    while True:
        speak("On which pin you want to operate:")
        pin_name = takeCommand().lower()  # Listen for pin name (like "base", "elbow", etc.)

        # Convert pin name to actual pin number
        pin_map = {
            "base": base,
            "shoulder": shoulder,
            "elbow": elbow,
            "wrist": wrist,
            "grip": grip
        }

        # Validate pin input
        if pin_name not in pin_map:
            speak("Invalid pin name. Please say base, shoulder, elbow, wrist, or grip.")
            continue

        speak("Angle please:")  # Ask user for angle
        try:
            angle = float(w2n.word_to_num(takeCommand().lower()))  # Convert spoken angle to float
            rotateServo(pin_map[pin_name], angle)  # Rotate servo
        except:
            speak("Sorry, I could not understand the angle. Please try again.")
