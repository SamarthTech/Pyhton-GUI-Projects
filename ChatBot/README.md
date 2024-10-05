# Documentation: app.py - AI Chatbot with Multiple Database Support

=====================================

This Python script powers a simple AI chatbot application built using Flask and ChatterBot, now extended to support multiple databases for storage. This document provides an overview of the code, explaining how it works and how the multiple database configuration is implemented.

=====================================

CODE BREAKDOWN

1. __Imports__

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

=====================================

# Flask is imported to create a web application.
# ChatterBot is the chatbot engine that powers the AI conversations.
# ChatterBotCorpusTrainer is used to train the chatbot on predefined datasets (corpus) in English

=====================================

2. __Flask Application Initialization__

app = Flask(__name__)

# The Flask class is instantiated, creating the core of our web application. This app object will manage the routing and responses of the web server.
#  The name parameter is set to the current module name (__name__), which is a common practice to avoid
#  potential issues with Flask's internal workings.

====================================

3. __Creating the Chatbot with Multiple Database__

def create_chatbot(database_uri):
    chatbot = ChatBot(
        "Chatterbot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=database_uri
    )
    return chatbot

# This create_chatbot() function is used to create a ChatterBot instance with a dynamic database_uri parameter.
# The storage_adapter specifies the type of database the chatbot will use for storing conversation data. By default, SQLStorageAdapter is used for SQL databases (SQLite, MySQL, PostgreSQL).
# The database_uri can now be customized by the user to point to different databases, providing flexibility.

=====================================

4. __Training the Chatbot__

database_uri = 'sqlite:///database.sqlite3'  # Default to SQLite
englishBot = create_chatbot(database_uri)
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")

# database_uri is initially set to use SQLite as the default database.
#  The create_chatbot() function is called to create a chatbot instance with the specified database.
#  The chatbot is created by calling create_chatbot(database_uri), passing the database URI into the function. This makes the database customizable.
# ChatterBotCorpusTrainer is used to train the chatbot with a predefined corpus of English language data. The train() method loads the training data to make the chatbot capable of responding to common queries in English.

=====================================

5. __Defining Flask Routes__

@app.route("/")
def index():
    return render_template("index.html")

# / Route: This route serves the homepage of the application, rendering the index.html template which contains the user interface for interacting with the chatbot.

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

# /get Route: This route handles the user input sent from the frontend via an AJAX request.
userText is the message sent by the user.
# get_response() is called to generate a response based on the user’s input, which is then returned to the frontend for display.


====================================

6. __Dynamic Database Configuration via Environment Variables__

# The database_uri variable can be customized using environment variables or passed through other methods, allowing users to switch databases without modifying the code directly.

# SQLite ( DEFAULT )

database_uri = 'sqlite:///database.sqlite3'

# MYSQL 

database_uri = 'mysql://username:password@localhost/db_name'

# PostgreSQL

database_uri = 'postgresql://username:password@localhost/db_name'

===================================

7. __Running the Application__

if __name__ == "__main__":
    app.run()

# The script uses the standard Python pattern to start the Flask development server. When you run the script, the web server will start, and the application will be accessible via http://127.0.0.1:5000.

===================================

**How the Multiple Database Support Works**

In the original app.py, the ChatterBot instance was hardcoded to use SQLite. After the modifications, we've introduced a function create_chatbot() that allows flexible database configuration.

Key Changes:

1. Dynamic Database URI: The database_uri can be changed based on the user’s preference or environment. This allows support for SQLite, MySQL, PostgreSQL, or any other database supported by ChatterBot.

2. Customization: You can now easily switch between databases for storing the chatbot’s training and conversation history, which is useful for different deployment environments (development, testing, production).

Benefits of This Change:

1. Scalability: Users can deploy the chatbot with different databases based on their system requirements.

2. Flexibility: Supports development with lightweight databases like SQLite and can be switched to production databases like MySQL/PostgreSQL without major code changes.

3. Customization: Developers can adapt the chatbot for different use cases by using various database configurations.

====================================






