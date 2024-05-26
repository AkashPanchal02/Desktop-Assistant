
from engine import *
import wikipedia
import webbrowser
import pywhatkit


def searchYoutube(query):
    if 'youtube' in query:
        speak("Searching on YouTube..")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)       # Opens searched query on youtube
        pywhatkit.playonyt(query)  # Plays the very first song in the list.


def searchGoogle(query):
    print("This is what i found on Google.")
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=2)
        # print(result)
        # speak(result)
    except:
        speak("This is what i found on Google.")


def searchWikipedia(query):
    speak("Searching Wikipedia")
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)