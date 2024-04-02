
from flask import Blueprint, request, render_template
from controllers.EmotionControllers.get_emotion_by_text import get_emotion_by_text
from controllers.EmotionControllers.get_emotion_by_image import get_emotion_by_image
from controllers.EmotionControllers.chat_generator_falcon import chat_generator_falcon
from controllers.EmotionControllers.chat_generator_llama2 import chat_generator_llama
import asyncio

emotionRouters = Blueprint('emotionRouters', __name__)

@emotionRouters.route('/api/emotion/get/text', methods=['POST'])
async def emotion_fun1():
        return await get_emotion_by_text()

@emotionRouters.route('/api/emotion/get/image', methods=['POST'])
async def emotion_fun2():
        return await get_emotion_by_image()

@emotionRouters.route('/api/emotion/chat/falcon', methods=['POST'])
async def falcon():
        return await chat_generator_falcon()


@emotionRouters.route('/api/emotion/chat/llama', methods=['POST'])
async def llama():
        return await chat_generator_llama()