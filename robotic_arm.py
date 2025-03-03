from pyfirmata import Arduino, SERVO
from time import sleep
import pyttsx3
import speech_recognition as sr
from word2number import w2n

port = 'COM3'
base = 9
shoulder = 10
elbow = 11
wrist = 12
grip = 13
board = Arduino(port)

board.digital[base].mode = SERVO 
board.digital[shoulder].mode = SERVO
board.digital[elbow].mode = SERVO
board.digital[wrist].mode = SERVO
board.digital[grip].mode = SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio, rate = 150):
    engine.setProperty('rate',rate)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes input as voice from the user and returns a string output 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        speak("On Which pin you want to operate:")
        pin = takeCommand().lower()
        speak("Angle please:")
        angle = float(w2n.word_to_num(takeCommand().lower()))
        rotateServo(pin, angle)