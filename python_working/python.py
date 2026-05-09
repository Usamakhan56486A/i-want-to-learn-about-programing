import pyttsx3 
import speech_recognition as sr


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',160)


def speak (command):
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

speak('''hi

''')


