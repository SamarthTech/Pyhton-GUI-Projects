import os
import speech_recognition as sr
import time
import pyautogui

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()


while True:
    query = takecommand()
    if ('wake up' in query or 'wakeup' in query or 'hello' in query) or ('jarvis' in query):
        os.startfile('E:\\JARVIS\\Jarvis UI 2\\Jarvis.py')
        time.sleep(8)
        pyautogui.click(1350, 325, button='left')
        exit()
    else:
        pass
