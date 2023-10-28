import pyttsx3
import speech_recognition as sr
from mutagen.mp3 import MP3
import os
import random
import time
import pyautogui
import mouse

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f"A.I : {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "none"
        
    return query.lower()

def Music():
    
    try:
        time.sleep(4 )
        pyautogui.hotkey('lctrl','b')


    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Music()
        else:
            Speak("no problem sir")


pyautogui.hotkey('winleft','r')
time.sleep(1)
Speak("Playing Music in 10 seconds Sir")
pyautogui.write("mswindowsmusic:")
pyautogui.press('enter')
Speak("Playing Music in 10 seconds Sir")
Music()
pid = os.getpid()
while True:
    query = (takecommand().lower()).replace("the ", "")
    if 'stop' in query:  
        Speak("Ok Sir, stopping the music.")
        pyautogui.hotkey('winleft','r')
        time.sleep(1)
        pyautogui.write("mswindowsmusic:")
        pyautogui.press('enter')
        time.sleep(4)
        time.sleep(3)
        pyautogui.click(4000,3,button='left')
        os.kill(pid, 0)
    elif "next" in query or "change" in query:
        Speak("Ok Sir, playing the next song.")
        pyautogui.hotkey('winleft','r')
        time.sleep(1)
        pyautogui.write("mswindowsmusic:")
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.hotkey('lctrl','f')
    elif "previous" in query or "last" in query:
        Speak("Ok Sir, playing the previous song.")
        pyautogui.hotkey('winleft','r')
        time.sleep(1)
        pyautogui.write("mswindowsmusic:")
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.hotkey('lctrl','b')
    
    else:
        pass