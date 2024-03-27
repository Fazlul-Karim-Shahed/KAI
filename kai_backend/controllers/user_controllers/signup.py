
from flask import request, jsonify, make_response
from models.user_model import User
# from passlib.hash import bcrypt

async def signup():
    try:
        from app import database
        data = request.get_json()

        check = database.user.find_one({"email": data["email"]})

        if check is None:
            # hash = bcrypt.hash(data["password"])
            
            return jsonify({"message": "Success", "error": False})
        else:
            return jsonify({'message': "User already exist", 'error': True})

        # user = User(data['username'], data['email'], data['password']).get()
        # new_user = database.user.insert_one(user)
        # return jsonify({'message': "New user added successfully", 'error': False})
    
    except Exception as err:
        return jsonify({"message": str(err), "error": True })