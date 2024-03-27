
from flask import Blueprint, request, render_template
from functions.tinilama import textGen
import asyncio

kai_chat = Blueprint('kai_chat', __name__)

@kai_chat.route('/api/kai-chat', methods=['GET', 'POST'])
async def my_function():
        
        from app import database
        db_messages = database.testKai
        
        if request.method == 'POST':

            data = db_messages.insert_one(
                {
                "role": "user",
                "content": request.form['user-inp']
                }
            )

            reply = await textGen(list(db_messages.find()))

            db_messages.insert_one({
                "role": "assistant",
                "content": reply,
            })

            messages = list(db_messages.find())

            return render_template('chat.html', **locals())
        

        elif request.method == 'GET':
            messages = list(db_messages.find())
            return render_template('chat.html', **locals())