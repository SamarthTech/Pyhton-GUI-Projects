import time
import webbrowser as web
import pyttsx3
import time
import keyboard
from pynput.keyboard import Key, Controller
import speech_recognition as sr
from whatsapp_read import whatsapp_find
import mouse
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(Text):
    print("   ")
    print(f"A.I : {Text}")
    engine.say(Text)
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



def Whatsapp(query):
    try:
        query = query.replace("jarvis ","").replace("send ","").replace("whatsapp ","").replace("message ","").replace("to ","").replace("please ","")
        numb = whatsapp_find(query.lower())
        
        if numb == 0:
            Speak("Record not found Sir.")
            Speak("Please tell me the number Sir.")
            numb = "+91" +takecommand().replace(" ","")
            if numb == "none":
                while True:                   
                    Speak("Please tell me the number Sir.")
                    numb = "+91" + takecommand().replace(" ","")
                    if numb != "none":
                        break
                    else:
                        continue
            Speak(f"Sending message to {numb} Sir....")
            Speak(f"What message should I send to {numb} Sir?")
        else:
            Speak(f"Sending message to {query} Sir....")
            Speak(f"What message should I send to {query} Sir?")
        mess = takecommand()
        Speak("Sending message in 30 seconds sir...")
        time.sleep(7)
        open_chat = "https://wa.me/" + numb
        web.open(open_chat)
        time.sleep(7)
        kb = Controller()
        kb.press(Key.left)
        kb.release(Key.left)
        keyboard.press('enter')
        time.sleep(15)
        keyboard.write(mess)
        keyboard.press('enter')
        Speak("Message Successfully sent Sir")

    except:
        Speak("Sorry sir, an error occured.")







