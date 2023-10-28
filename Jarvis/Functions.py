
import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from mutagen.mp3 import MP3
import time
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
import speedtest
from playsound import playsound
import keyboard 
import pyjokes
from PyDictionary import PyDictionary as Diction
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
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





def MusicFromYt():
    try:
        Speak("Tell Me The NamE oF The Song Sir!")
        musicName = takecommand().lower()
        if musicName == "none":
                while True:                   
                    Speak("Please tell me the name of the music Sir.")
                    musicName = takecommand().lower()
                    if musicName != "none" or musicName == "exit":
                        break
                    else:
                        continue
        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Music()
        else:
            Speak("no problem sir")


def SpeedTest():
    try:
        Speak("Checking Speed Sir...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUp = int(uploading/800000)
        Speak(f"Sir, the downloading speed is {correctDown} Mbps and the uploading speed is {correctUp} Mbps.")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            SpeedTest()
        else:
            Speak("no problem sir")


def Music():
    os.startfile("E:\\JARVIS\\Music.py")


def OpenApps(query):
    try:
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile(r"C:\Users\User_Name\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif 'spotify' in query:
            webbrowser.open('https://open.spotify.com/')

        elif 'telegram' in query:
            webbrowser.open('https://web.telegram.org/z/')


        elif 'whatsapp' in query:
            os.startfile(r"C:\Users\User_Name\AppData\Local\WhatsApp\WhatsApp.exe")

        elif 'word' in query or 'micorsoft word' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")    

        elif 'edge' in query or 'microsoft edge' in query:
            os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'google drive' in query or 'drive' in query:
            webbrowser.open('https://www.drive.google.com/')

        elif 'maps' in query or 'google maps' in query:
            webbrowser.open('https://www.maps.google.com')

        elif 'mail' in query or 'gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/')

        elif 'google classroom' in query or 'classroom' in query:
            webbrowser.open('https://classroom.google.com/u/0/h')

        elif 'mkvcinemas' in query:
            webbrowser.open('mkvcinemas.pl')

        elif 'google' in query:
            webbrowser.open('https://www.google.com')
        elif 'wifi' in query:
            webbrowser.open('http://172.17.96.65/0/up')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif '1mg' in query:
            webbrowser.open('1mg.com/')

        elif 'python' in query:
            os.startfile(r"C:\\Users\\User_Name\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\idle.pyw")

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            OpenApps(query)
        else:
            Speak("no problem sir")


def Temp():
    try:
        search = "temperature in kolkata"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature}")
        a = 1
        while a == 1:
            Speak("Do I Have To Tell You the Temperature of any other place Sir?")
            next = takecommand()

            if 'yes' in next:
                Speak("Tell Me The Name Of tHE Place Sir.")
                name = takecommand()
                search = f"temperature in {name}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temperature = data.find("div",class_ = "BNeawe").text
                Speak(f"The Temperature in {name} is {temperature}.")

            else:
                a = 0
                Speak("no problem sir")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Temp()
        else:
            Speak("no problem sir")


def Dict():
    try:
        Speak("Activated Dictionary Sir!")
        Speak("Tell me the problem Sir.")
        prob = takecommand().lower()
        if prob == "none":
                while True:                   
                    Speak("Please tell me the problem Sir.")
                    prob = takecommand().lower()
                    if prob != "none":
                        break
                    else:
                        continue

        if 'meaning' in prob:
            prob = prob.replace("what is the", "").replace("jarvis", "").replace("of", "").replace("meaning", "")
            result = Diction.meaning(prob)
            Speak(f"The meaning of {prob} is {result}")

        elif 'synonyms' in prob:
            prob = prob.replace("what is the", "").replace("jarvis", "").replace("of", "").replace("synonyms", "")
            result = Diction.synonym(prob)
            Speak(f"The synonym of {prob} is {result}")

        elif 'antonyms' in prob:
            prob = prob.replace("what is the", "").replace("jarvis", "").replace("of", "").replace("antonyms", "")
            result = Diction.antonym(prob)
            Speak(f"The antonym of {prob} is {result}")
        Speak("Exited Dictionary!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Dict()
        else:
            Speak("no problem sir")


def Reader():
    try:
        Speak("Please enter the location of the PDF file you want me to read Sir.")
        location=input("Enter the location here Sir: ")
        location = location.replace('"', '').replace("'","")
        os.startfile(location)
        book = open(location,'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()
        Speak(f"Number Of Pages In This pdf Are {pages}")
        Speak("From Which Page shall I Start Reading SIr?")
        numPage = int(input("Enter The Page number here:"))
        numPage = numPage - 1
        Speak("Starting to read in 8 seconds or earlier Sir.")
        time.sleep(4)
        for j in range(numPage, pages):
            page = pdfreader.getPage(j)
            text = page.extractText()
            Speak(text)
            d = ['.',',','?','!',';',':']
            for i in d:
                if i in text:
                    time.sleep(0.5)
                else:
                    pass
    
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Reader()
        else:
            Speak("no problem sir")


def CloseAPPS(query):
    try:

        Speak("Ok Sir , Wait A second!")
        
        if 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'whatsapp' in query:
            os.system("TASKKILL /F /im WhatsApp.exe")

        elif 'word' in query or 'microsoft word' in query:
            os.system("TASKKILL /F /im WINWORD.exe")
        
        elif 'edge' in query or 'microsoft edge' in query:
            os.system("TASKKILL /F /im msedge.exe")

        elif 'python' in query:
            os.system("TASKKILL /F /im idle.pyw")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

            
        Speak("Your Command Has Been Succesfully Completed!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            CloseAPPS(query)
        else:
            Speak("no problem sir")


def YoutubeAuto():
    try:
        Speak("Youtube Automation started!")
        Speak("Whats Your Command Sir?")
        comm = takecommand().lower()
        if comm == "none":
                while True:                   
                    Speak("Please tell me Your Command Sir")
                    comm = takecommand().lower()
                    if comm != "none":
                        break
                    else:
                        continue

        if 'pause' in comm or 'play' in comm:
            keyboard.press('k')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')
        
        elif 'captions' in comm or 'caption' in comm:
            keyboard.press('c')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'search' in comm:
            keyboard.press('/')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            YoutubeAuto()
        else:
            Speak("no problem sir")


def Alarm(query):
    query = str(query).lower()
    TimeHEre = open("E:\\JARVIS\\Data.txt", 'a')
    TimeHEre.write(query)
    TimeHEre.close()
    os.startfile("E:\\JARVIS\\Alarm.py")

def VideoDownloader():
    try:
        root = Tk()
        root.geometry('500x300')
        root.resizable(0,0)
        root.title("Youtube Video Downloader")
        Speak("Enter Video Url Here !")
        Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
        link = StringVar()
        Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
        Entry(root,width = 70,textvariable = link).place(x=32,y=90)

        def VideoDownloader():
            url = YouTube(str(link.get()))
            video = url.streams.first()
            video.download()
            Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

        Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

        root.mainloop()
        Speak("Video Downloaded")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            VideoDownloader()
        else:
            Speak("no problem sir")


def ChromeAuto():
    try:
        Speak("Chrome Automation started!")
        Speak("Whats Your Command Sir?")
        command = takecommand().lower()
        if command == "none":
                while True:                   
                    Speak("Please tell me Your Command Sir?")
                    command = takecommand().lower()
                    if command != "none":
                        break
                    else:
                        continue

        if 'close' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command or ('open' in command and 'tab' in command):
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command or ('open' in command and 'window' in command):
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'downloads' in command or 'download' in command:
            keyboard.press_and_release('ctrl + j')

        Speak("Done Sir")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            ChromeAuto()
        else:
            Speak("no problem sir")


def screenshot():
    try:
        Speak("Ok Boss , What Should I Name That File ?")
        path = takecommand().lower()
        if path == "none":
                while True:                   
                    Speak("Please tell me what Should I Name That File Boss.")
                    path = takecommand().lower()
                    if path != "none":
                        break
                    else:
                        continue
        kk = pyautogui.screenshot()
        kk.save(f"E:/JARVIS/Jarvis UI 2/Screenshots/"+ path + ".jpg")
        os.startfile(f"E:/JARVIS/Jarvis UI 2/Screenshots/"+ path + ".jpg")
        Speak("ScreenShot taken Sir.") 
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            screenshot()
        else:
            Speak("no problem sir")


def Note_Reminder(query):
    try:
        remeberMsg = query.replace("remember that","")
        remeberMsg = remeberMsg.replace("jarvis","")
        Speak("You Told Me To Remind You That :"+remeberMsg)
        remeber = open('data.txt','w')
        remeber.write(remeberMsg)
        remeber.close()
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Note_Reminder()
        else:
            Speak("no problem sir")


def YoutubeSearch(query):
    try:
        Speak("Ok Sir , This is what I found for your search!")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        Speak("Done Sir!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            YoutubeSearch()
        else:
            Speak("no problem sir")


def Website_with_Open(query):
    try: 
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Website_with_Open()
        else:
            Speak("no problem sir")


def Website_with_Launch():
    try:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = "https://www." + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Website_with_Launch()
        else:
            Speak("no problem sir")


def Wikipedia_Search(query):
    try:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Wikipedia_Search()
        else:
            Speak("no problem sir")


def Time():
    try:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir the time is {strTime}")
        Speak(f"Sir the time is {strTime}")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Time()
        else:
            Speak("no problem sir")


def Joke():
    try:
        get = pyjokes.get_joke()
        Speak(get)
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Joke()
        else:
            Speak("no problem sir")


def Repeat_word():
    try:
            Speak("Speak Sir")
            jj = takecommand()
            Speak(f"You Said : {jj}")
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Repeat_word()
        else:
            Speak("no problem sir")


def Open_Location():
    try:
        Speak("Ok Sir , Wait A Second!")
        webbrowser.open('https://www.google.com/maps/@19.1334302,72.9110792,17z')
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Open_Location()
        else:
            Speak("no problem sir")


def Remind():
    try:
            remeber = open('data.txt','r')
            r = remeber.readlines()
            for i in r:
                Speak("You Told Me to remind you That", i )
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            Remind()
        else:
            Speak("no problem sir")


def AskAnything(query):
    try:
            Speak("Getting Data From The Internet Sir!")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) is 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
    except:
        Speak("Sorry sir, an error occured.")
        Speak("Do you want to try that again?")
        choice = takecommand().lower()
        if 'yes' in choice:
            AskAnything()
        else:
            Speak("no problem sir")

def Google_Search(query):
    try:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("search google for","")
            query = query.replace("google","")
            query = query.replace("what is","").replace("?", "")
            Speak("This Is What I Found On The Web!") 
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Data Found!")
    except:
        Speak("Sorry Sir, no speakable data found. Please try again.")

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        Speak("Good Morning Sir!")
        Speak("How may I help you?")
    elif hour>=12 and hour<16:
        Speak("Good Afternoon Sir!")
        Speak("How may I help you?")
    elif hour>=16 and hour<=23:
        Speak("Good Evening Sir!")
        Speak("How may I help you?")
    elif hour>=0 and hour<5:
        Speak("Hello Sir! Its time for bed Sir. You should go to sleep")

