
from flask import request, jsonify, make_response


async def get_emotion_by_text():
    try:
        from transformers import pipeline

        data = request.get_json()

        classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
        prediction = classifier(data['prompt'])
        print(prediction)
        return jsonify({"message": "ok"})


        
    
    except Exception as err:
        return jsonify({"message": str(err), "error": True })