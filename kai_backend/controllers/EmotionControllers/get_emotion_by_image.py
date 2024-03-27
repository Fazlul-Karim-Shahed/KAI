
from flask import request, jsonify, make_response


async def get_emotion_by_image():
    try:
        from transformers import pipeline

        data = request.get_json()

        pipe1 = pipeline("image-classification", model="dima806/facial_emotions_image_detection")
        prediction = pipe1(data['image'])
        print(prediction)
        return jsonify({"message": "ok"})


        
    
    except Exception as err:
        return jsonify({"message": str(err), "error": True })