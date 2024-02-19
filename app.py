from flask import Flask, render_template, request
from tinilama import textGen 
import asyncio
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017')
database = client.KAI



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/kai', methods=['GET', 'POST'])
async def kai_chat():
    if request.method == 'POST':

        reply = await textGen(request.form['user-inp'])
        print("The reply is: ", reply)
        # reply = request.form['user-inp']
        return render_template('chat.html', **locals())
    elif request.method == 'GET':
        
        return render_template('chat.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
