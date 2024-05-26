
import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 190)    # Control Fluency speed


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 300      # Very low value can also listen background voice
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f'You Said : {query}\n')
    except Exception as e:
        print("Please say that Again!")
        speak("Please say that Again!")
        return 'None'
    return query