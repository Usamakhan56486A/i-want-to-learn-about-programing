import pyttsx3 

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',160)


def speak (command):
    engine.say(command)
    engine.runAndWait()

speak('how are you ')