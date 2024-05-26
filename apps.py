
from engine import *
import pyautogui
import webbrowser
from time import sleep
import os

dictApp = {
    'command prompt': 'cmd',
    'paint': 'paint',
    'word': 'winword',
    'excel': 'excel',
    'chrome': 'chrome',
    'vs code': 'code',
    'powerpoint': 'powerpnt',
    'media player': 'Microsoft.Media.Player',
    'camera': 'ApplicationFrameHost',
    'microsoft edge': 'msedge'
}

def openApp(query):
    if '.com' in query or '.co.in' in query or'.org' in query or '.netlify.app' in query:
        query = query.replace('open', '')
        query = query.replace('wednesday', '')
        query = query.replace('launch', '')
        query = query.replace(' ', '')
        speak(f"Opening {query}")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"Start {dictApp[app]}")


def closeApp(query):
    if 'one tab' in query or '1 tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("One Tab Closed")
    elif 'two tab' in query or '2 tabs' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("Two Tabs Closed")
    elif 'three tabs' in query or '3 tabs' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        speak("Three Tabs Closed")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f'taskkill /f /im {dictApp[app]}.exe')

