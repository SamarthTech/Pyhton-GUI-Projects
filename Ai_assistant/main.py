import datetime
import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
from config import apikey
import os
import  random
import string

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Utsav: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]






def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))


    invalid_chars = '\\/:*?"<>|'
    prompt_filename = ''.join(c for c in prompt if c not in invalid_chars).strip()


    file_path = f"Openai\\{random_filename}_{prompt_filename}.txt"

    with open(file_path, "w") as f:
        f.write(text)
def say(text):
    engine = pyttsx3.init()
    engine.setProperty('device', '0')
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.pause_threshold = 1
        r.energy_threshold = 200

        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(query)
            return query
        except Exception as e:
            query="Some error occured"
            return query
if __name__ == '__main__':

    say("Hello I am Jarvis , Assistant of Master, Utsav !!")
    while True:
        print("Listening....")
        query=takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir ,the time is{strftime} ")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Exit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)