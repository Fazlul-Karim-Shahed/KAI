from flask import Flask, render_template, request
import asyncio
from pymongo import MongoClient
from routers.kai_chat_routers.kai_chat import kai_chat
from routers.UserRouters import userRouter
from routers.emotion_routers import emotionRouters

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017')
database = client.KAI

@app.route('/')
def hello_world():
    return 'Hello World!'

app.register_blueprint(kai_chat)
app.register_blueprint(userRouter)
app.register_blueprint(emotionRouters)



if __name__ == '__main__':
    app.run(debug=True, port=8000)
