from playsound import playsound
import datetime
import time as t
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):
    print("   ")
    print(f"A.I : {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

extracted_time = open("E:\\JARVIS\\Jarvis UI 2\\Data.txt", 'rt')
time = extracted_time.read()
Time = str(time)

delete_time = open("E:\\JARVIS\\Jarvis UI 2\\Data.txt", 'r+')
delete_time.truncate(0)
delete_time.close()


def RingerNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis ", "").replace("set ", "").replace("alarm ", "").replace("at ", "").replace("for ", "").replace(" and ", ":")

    Alarm_Time = str(time_now)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == Alarm_Time:
            Speak("Your alarm is ringing Sir")
            playsound("E:\\JARVIS\\Jarvis UI 2\\tone.mp3")
            t.sleep(4)
        elif current_time > Alarm_Time:
            Speak("Alarm stopped sir.")
            exit()

            
RingerNow(Time)
