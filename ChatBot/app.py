#imports
import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Load database configuration from environment variables
db_adapter = os.getenv('DB_ADAPTER', 'chatterbot.storage.SQLStorageAdapter')  # Default to SQLite
db_uri = os.getenv('DATABASE_URI', None)  # Optional: Database URI for non-SQLite databases

# Create chatbot with dynamic database configuration
if db_uri:
    englishBot = ChatBot("Chatterbot", storage_adapter=db_adapter, database_uri=db_uri)
else:
    englishBot = ChatBot("Chatterbot", storage_adapter=db_adapter)

trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")  # Train the chatbot with English corpus

# Define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
# Function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()
