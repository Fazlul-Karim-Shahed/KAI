
from flask import Blueprint, request, render_template
from controllers.EmotionControllers.get_emotion_by_text import get_emotion_by_text
from controllers.EmotionControllers.get_emotion_by_image import get_emotion_by_image
import asyncio

emotionRouters = Blueprint('emotionRouters', __name__)

@emotionRouters.route('/api/emotion/text', methods=['POST'])
async def emotion_fun1():
        return await get_emotion_by_text()

@emotionRouters.route('/api/emotion/image', methods=['POST'])
async def emotion_fun2():
        return await get_emotion_by_image()