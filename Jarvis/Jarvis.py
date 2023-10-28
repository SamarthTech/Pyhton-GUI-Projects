
from xml.etree.ElementTree import tostring
from JarvisUi_2 import Ui_JarvisUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import os
import webbrowser as web
import sys
import pyttsx3
import speech_recognition as sr
import whatsapp
import os
from datetime import datetime
from datetime import date
import Chatbot
import Functions
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def Speak(Text):
    print("   ")
    print(f"A.I : {Text}")
    engine.say(Text)
    print("    ")
    engine.runAndWait()


class MainThread(QThread):

    def __init__(self):

        super(MainThread, self).__init__()


    def run(self):
        self.TaskGui()

    
    def takecommand(self): 
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
            return ""
            
        return query.lower()


    def TaskGui(self):


        Functions.WishMe()

        while True:

            self.query = self.takecommand().lower()

            

            if 'google search' in self.query or 'search google' in self.query:
                Functions.Google_Search(self.query)

            elif "pause" in self.query or "resume" in self.query :
                if "pause" in self.query:
                    if  "music" in self.query or "video" in self.query or "song" in self.query or "movie" in self.query or "media" in self.query:
                        a = self.query.lower().replace("jarvis", "").replace("pause", "").replace("the", "").replace(" ", "")
                        pyautogui.press('playpause')
                        Speak(f"{a} paused sir.")
                    else: 
                        pass
                elif "resume" in self.query:
                    if  "music" in self.query or "video" in self.query or "song" in self.query or "movie" in self.query or "media" in self.query:
                        a = self.query.lower().replace("jarvis", "").replace("resume", "").replace("the", "").replace(" ", "")
                        pyautogui.press('playpause')
                        Speak(f"{a} resumed sir.")
                    else: 
                        pass

            elif "volume" in self.query:
                if "reduce" in self.query or "down" in self.query or "lower" in self.query:
                    pyautogui.press("volumedown", presses = 3)
                    Speak("Volume decreased sir.")
            
                elif "mute" in self.query:
                    Speak("Muting volume sir.")
                    pyautogui.press("volumemute")
                
                elif "volume up" in self.query or "increase the volume" in self.query or "increase volume" in self.query  or "volumeup" in self.query:
                    pyautogui.press("volumeup", presses = 2)
                    Speak("Volume increased sir.")
                else:
                    pass
                
            elif "my mix" in self.query or "my playlist" in self.query:
                web.open('https://www.youtube.com/watch?v=3wkPgFrM36o&list=PLZ03MG4mq-eEzpw412Pqoubi8ZVCpbtqi')
                Speak("Playing your favourite playlist on youtube sir.")

            elif "hindi song playlist" in self.query or "hindi songs playlist" in self.query or "hindi songs" in self.query or "hindi song" in self.query or "hindi music" in self.query:
                web.open('https://www.youtube.com/watch?v=OuNGySNJjWg&list=RDOuNGySNJjWg&start_radio=1')
                Speak("Playing your hindi songs playlist on youtube sir.")
                
            elif "alan walker playlist" in self.query or "alan walker music" in self.query or "alan walker song" in self.query or "alan walker songs" in self.query:
                web.open('https://www.youtube.com/watch?v=GeXIx_4_Hvo&list=RDGeXIx_4_Hvo&start_radio=1')
                Speak("Playing your Alan Walker playlist on youtube sir.")
            
            elif 'music' in self.query or 'song' in self.query or 'songs' in self.query:
                if 'from' in self.query:
                    Functions.MusicFromYt()
                else:
                    Functions.Music()



            elif "bye Jarvis" in self.query or "take a break" in self.query or 'bye' in self.query or "good bye" in self.query or "goodbye"in self.query or "see you later" in self.query or "exit" in self.query or "bye jarvis" in self.query or "leaving now" in self.query or "leave now" in self.query or "shutdown" in self.query or "shut down" in self.query or "sleep" in self.query or "good bye jarvis" in self.query or "goodbye jarvis" in self.query:                     
                reply = Chatbot.Chatterbot(self.query)
                Speak(reply)
                exit(GuiApp.exec_())

            elif 'how are you' in self.query:
                Speak("I Am Fine Sir!")
                Speak("Whats About YOU?")
            
            elif 'youtube search' in self.query:
                Functions.YoutubeSearch(self.query)
                
            elif 'website' in self.query:
                Functions.Website_with_Open(self.query)

            elif 'launch' in self.query:
                Functions.Website_with_Launch()

            elif 'wikipedia' in self.query:
                Functions.Wikipedia_Search(self.query)

            elif 'whatsapp message' in self.query:
                os.startfile(r"C:\Users\User_Name\AppData\Local\WhatsApp\WhatsApp.exe")
                whatsapp.Whatsapp(self.query)

            elif 'screenshot' in self.query:
                Functions.screenshot()

            elif 'open facebook' in self.query:
                Functions.OpenApps(self.query)

            elif 'google drive' in self.query or 'drive' in self.query:
                Functions.OpenApps(self.query)

            elif 'time' in self.query:
                Functions.Time()

            elif 'open whatsapp' in self.query:
                Functions.OpenApps(self.query)

            elif 'open spotify' in self.query:
                Functions.OpenApps(self.query)

            elif 'open word' in self.query or 'microsoft word' in self.query:
                Functions.OpenApps(self.query)

            elif 'open edge' in self.query or 'microsoft edge' in self.query:
                Functions.OpenApps(self.query)          

            elif 'open maps' in self.query or 'open google maps' in self.query:
                Functions.OpenApps(self.query)

            elif 'open google classroom' in self.query or 'open classroom' in self.query:
                Functions.OpenApps(self.query)

            elif 'open google' in self.query:
                Functions.OpenApps(self.query)

            elif 'open youtube' in self.query:
                Functions.OpenApps(self.query)

            elif 'open python' in self.query:
                Functions.OpenApps(self.query)

            elif 'open mkvcinemas' in self.query:
                Functions.OpenApps(self.query)
            
            elif 'open gmail' in self.query:
                Functions.OpenApps(self.query)

            elif 'open wifi' in self.query or 'wifi' in self.query:
                Functions.OpenApps(self.query)

            elif 'open 1mg' in self.query:
                Functions.OpenApps(self.query)  

            elif 'open instagram' in self.query:
                Functions.OpenApps(self.query)

            elif 'open code' in self.query:
                Functions.OpenApps(self.query)

            elif 'open youtube' in self.query:
                Functions.OpenApps(self.query)
                
            elif 'open telegram' in self.query:
                Functions.OpenApps(self.query)

            elif 'open chrome' in self.query:
                Functions.OpenApps(self.query)


            elif 'close chrome' in self.query:
                Functions.CloseAPPS(self.query)

            elif 'close code' in self.query:
                Functions.CloseAPPS(self.query)

            elif 'close python' in self.query:
                Functions.CloseAPPS(self.query)

            elif 'close whatsapp' in self.query:
                Functions.CloseAPPS(self.query)

            elif 'close word' in self.query or 'close microsoft word' in self.query:
                Functions.CloseAPPS(self.query)

            elif 'close edge' in self.query or 'close microsoft edge' in self.query:
                Functions.CloseAPPS(self.query)


            elif 'youtube tool' in self.query or 'automate youtube' in self.query:
                Functions.YoutubeAuto()

            elif 'chrome automation' in self.query or 'chrome tool' in self.query:
                Functions.ChromeAuto()

            elif 'joke' in self.query:
                Functions.Joke()

            elif 'repeat my word' in self.query:
                Functions.Repeat_word()

            elif 'my location' in self.query:
                Functions.Open_Location()

            elif 'alarm' in self.query:
                Functions.Alarm(self.query)

            elif 'video downloader' in self.query:
                Functions.VideoDownloader()
            
            elif 'what do you remember' in self.query or 'remind' in self.query or 'any reminder' in self.query or 'any reminders' in self.query:
                Functions.Remind()

            elif 'remember that' in self.query or 'reminder' in self.query:
                Functions.Note_Reminder()

            
            elif 'how to' in self.query:
                Functions.AskAnything(self.query)
                
            elif 'temperature' in self.query:
                Functions.Temp()

            elif 'read' in self.query:
                Functions.Reader()

            elif 'dictionary' in self.query:
                Functions.Dict()
            
            elif 'speed' in self.query  and ('check' in self.query or 'internet' in self.query):
                Functions.SpeedTest()
            
            elif 'what is' in self.query:
                Functions.Google_Search(self.query)

            elif 'stop music' in self.query  or 'stop the music' in self.query or 'stop song' in self.query or 'stop the song' in self.query:
                pass
            
            else: 
                reply = Chatbot.Chatterbot(self.query)
                if reply != 0:
                    Speak(reply)
                elif self.query != "none":
                    pass



    

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisUI()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)
        self.gui.pushButton_chrome.clicked.connect(self.chrome_app)
        self.gui.pushButton_whatsapp.clicked.connect(self.whatsapp_app)
        self.gui.pushButton_yt.clicked.connect(self.yt_app)

    
    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        os.startfile(r"C:\Users\User_Name\AppData\Local\WhatsApp\WhatsApp.exe")


    def startTask(self):

        self.gui.movies1 = QtGui.QMovie(f"E:\JARVIS\Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.movies1)
        self.gui.movies1.start()

        self.gui.movies2 = QtGui.QMovie(f"E:\JARVIS\live.gif")
        self.gui.Gif_2.setMovie(self.gui.movies2)
        self.gui.movies2.start()

        self.gui.movies3 = QtGui.QMovie(f"E:\JARVIS\__1.gif")
        self.gui.Gif_3.setMovie(self.gui.movies3)
        self.gui.movies3.start()

        self.gui.movies4 = QtGui.QMovie(f"E:\JARVIS\Earth.gif")
        self.gui.Gif_4.setMovie(self.gui.movies4)
        self.gui.movies4.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        
    
        startExe.start()


    def showTimeLive(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S") 
        date = now.strftime("%d/%m/%Y")
        label_time = "Time: " + time
        label_date = "Date: " + date
        label_day = datetime.today().strftime('%A')
        self.gui.Text_Time.setText(label_time)
        self.gui.Text_Date.setText(label_date)
        self.gui.Text_Day.setText(label_day)




GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())


