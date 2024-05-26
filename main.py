
from engine import *
import datetime
from time import sleep
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import requests 
import os
import random
from bs4 import BeautifulSoup
import speedtest


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('Good Morning')
    elif hour >= 12 and hour <= 18:
        speak('Good Afternoon')
    else:
        speak("Good Evening")
    speak('I"m Wednesday. Tell me how can i help you.')
    

if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()

        if 'quit' in query:
            print("Quitting sir..! Thanks for using me, have a great day")
            speak("Quitting sir..! Thanks for using me, have a great day")
            exit()

        elif "hello"  in query or 'hey wednesday' in query:
            speak("Hello Sir, How are you ?")

        elif "i am fine what about you" in query:
            speak("That's Great. I'm also doing well, thank you! Tell me how can i help you ?")

        elif "what about you" in query:
            speak("I'm also doing well, thank you! How can i assist you.")

        elif "incognito" in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        
        elif "thank you" in query:
            speak("you are welcome")

        elif "play video" in query:
            pyautogui.press('k')
            speak("Video Played")

        elif "pause video" in query:
            pyautogui.press('k')
            speak("Video Paused")
        
        elif "mute video" in query:
            pyautogui.press('m')
            speak("Video Muted")
        
        elif "unmute video" in query:
            pyautogui.press('m')
            speak("Video Unmuted")
        
        elif "full screen" in query:
            pyautogui.press('f')

        elif 'volume up' in query:
            from keyboard import volumeUp
            speak("Volume Turned Up")            
            volumeUp()            

        elif 'volume down' in query:
            from keyboard import volumeDown
            speak("Volume Turned Down")            
            volumeDown()            

        elif 'open' in query:
            from apps import openApp
            openApp(query)
        
        elif 'close' in query:
            from apps import closeApp
            closeApp(query)

        elif 'google' in query:
            from searchNow import searchGoogle
            searchGoogle(query)

        elif "youtube" in query:
            from searchNow import searchYoutube 
            searchYoutube(query)

        elif "wikipedia" in query:
            from searchNow import searchWikipedia
            searchWikipedia(query)

        elif "temperature" in query:
            speak("Tell the city name to know its temperature : ")
            city = takeCommand() 
            url = f"https://www.google.com/search?q={city}+weather"
            r = requests.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            temp = data.find('div', class_='BNeawe').text
            speak(f"Current temprature of {city} is {temp}")
            print(f"Current temprature of {city} is {temp}")
            
        elif "weather" in query:
            speak("Tell the city name to know its weather : ")
            city = takeCommand()
            url = f"https://www.google.com/search?q={city}+weather"
            r = requests.get(url).content
            soup = BeautifulSoup(r, 'html.parser')
            temp = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
            sky_desc = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text

            data = sky_desc.split('\n')
            time = data[0]
            sky = data[1]

            list_div = soup.findAll('div', class_='BNeawe s3v9rd AP7Wnd')
            strd = list_div[5].text

            pos = strd.find('wind')
            speak("Weather details are as follows : ")
            print(f"Current {query} is: {temp} at: {time}, feels like: {sky}")
            speak(f"Current {query} is: {temp} at: {time}, feels like: {sky}")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is : {strTime}")

        elif 'play music' in query:
            speak("Playing Music")
            album = r"E:\Programming\Desktop Assistant\Music"
            songs = os.listdir(album)
            length = len(songs)
            randNo = random.randint(0, length)
            os.startfile(os.path.join(album,songs[randNo]))

        elif 'whatsapp' in query:
            contact = ['bro', 'Bro', 'mummy', 'Mummy', 'dad', 'Dad', 'Piyush', 'piyush']
        
            speak("Whom you want to send the message - ")
            person = takeCommand()

            if person in contact:    
                if person == "bro" or person == "Bro":
                    speak("What's the message sir - ")
                    message = takeCommand()
                    hrs = int(datetime.datetime.now().strftime('%H'))
                    mins = int(datetime.datetime.now().strftime('%M'))
                    pywhatkit.sendwhatmsg("+918929585927", message, hrs, mins + 1)

                elif person == "mummy" or person == "Mummy":
                    speak("What's the message sir - ")
                    message = takeCommand()
                    hrs = int(datetime.datetime.now().strftime('%H'))
                    mins = int(datetime.datetime.now().strftime('%M'))
                    pywhatkit.sendwhatmsg("+918199034560", message, hrs, mins + 1)

                elif person == "dad" or person == "Dad":
                    speak("What's the message sir - ")
                    message = takeCommand()
                    hrs = int(datetime.datetime.now().strftime('%H'))
                    mins = int(datetime.datetime.now().strftime('%M'))
                    pywhatkit.sendwhatmsg("+919319250020", message, hrs, mins + 1)

                elif person == "Piyush" or person == "piyush":
                    speak("What's the message sir - ")
                    message = takeCommand()
                    hrs = int(datetime.datetime.now().strftime('%H'))
                    mins = int(datetime.datetime.now().strftime('%M'))
                    pywhatkit.sendwhatmsg("+919991121301", message, hrs, mins + 1)

                else:
                    speak("Contact not added in the list")
        
        elif 'my gmail' in query:
            speak("Opening Gmail")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
        
        elif 'shutdown' in query:
            speak("Are you sure, You want to shut down the system.")
            shutdown = takeCommand()
            if shutdown == 'yes' or shutdown == 'Yes':
                os.system('shutdown /s /t 1')
            elif shutdown == 'no' or shutdown == 'No':
                break          

        elif 'internet speed' in query:
            print("Calculating .. Please wait for a while..")
            speak("Calculating .. Please wait for a while..")
            wifi = speedtest.Speedtest()
            uploadSpeed = round(wifi.upload()/(1024*1024), 2)
            downloadSpeed = round(wifi.upload()/(1024*1024), 2)
            print(f"Network upload speed is : {uploadSpeed} Mbps")
            print(f"Network download speed is : {downloadSpeed} Mbps")
            speak(f"Network upload speed is : {uploadSpeed} Mb P s")
            speak(f"Network download speed is : {downloadSpeed} Mb p s")
        
        elif 'screenshot' in query:
            ss = pyautogui.screenshot()
            ss.save('ss.jpg')
            speak("Captured Sir, It's saved with ss.jpg")
        
        elif 'take my photo' in query or 'capture my photo' in query or 'photo' in query:
            pyautogui.press('super')
            pyautogui.typewrite('camera')
            pyautogui.press('enter')
            sleep(2)
            speak('smile..')
            pyautogui.press('enter')

