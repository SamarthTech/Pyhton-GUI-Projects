import random

command_1 = ['hello', 'wakeup', 'you there', 'hey', 'hi', 'help me', "hello", "hey", "hi", "wake up", "wake up jarvis", 
"wakeup javis", "hii"]

reply_1 = ['Hello Sir, welcome back', "Hello Sir!", "How are you Sir?", "Always for you Sir!",
"Here is your assistant, Sir!", "Welcome back Sir, how can I help you?"
"Hi sir, is there any work for me?", "Hi sir, how are you?", "Nice meeting you again sir."]

command_2 = ["bye Jarvis", 'bye', "good bye", "goodbye", "see you later", "exit", "bye jarvis", "leaving now",
"leave now", "shut down", "sleep"]


reply_2 = ["Bye Sir!", "Ok Sir, see you later. Bye.", "Always for you Sir! Bye.", "Bye Sir. It was nice helping you Sir!", 
"Good Bye Sir!", "Bye Sir, if you want me back again, just say wake up jarvis!", "as you wish Sir, Bye!"]

def Chatterbot(text):
    for word in text.split(' '):
        if word in command_1:
            return random.choice(reply_1)
        elif word in command_2:
            return random.choice(reply_2)
        else: 
            return 0

