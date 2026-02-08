import webbrowser
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
recognizer=sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def openwebsites(c):
    if "open google" in c.lower():
        webbrowser.open_new("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open_new("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open_new("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open_new("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open_new("https://linkedin.com")
if __name__=="__main__":
    speak("Hii i'm Jarvis,i'm initialising....")
    while True:
        r=sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source, timeout=3, phrase_time_limit=5)
            command=r.recognize_google(audio)
            if command.lower()=="jarvis":
                speak("Yeh hii how can i help u")
                with sr.Microphone() as source:
                    print("Listening....")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                openwebsites(command)
        except Exception as e:
            print("Error;{0}".format(e))
