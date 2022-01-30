import speech_recognition as sr
import pywhatkit
import pyttsx3
engine = pyttsx3.init()
# sound = engine.getProperty('voices')
# engine.setProperty('voice', sound[0].id)
rate = engine.getProperty("rate")
engine.setProperty("rate",160)
engine.say("Please say something I will play that for you on youtube...")
engine.runAndWait()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        choice = text
        engine.say("Plaing "+choice+" on youtude...")
        engine.runAndWait()
        pywhatkit.playonyt(choice)
    except:
        engine.say("Sorry I couldn't recognize what you say...")
        engine.runAndWait()
