
import re

class User:
    def __init__(self, username:str, email:str, password:str):

        if not username or not password or not email:
            raise ValueError("Missing required value")
        
        if not isinstance(username, str):
            raise ValueError("username must be strings")
        
        if not isinstance(email, str):
            raise ValueError("email must be strings")
        
        if not isinstance(password, str):
            raise ValueError("password must be strings")
        
        if len(username) < 5:
            raise ValueError("username must be at least 5 characters long")
        
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Invalid email address')

        if not (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in r'!@#$%^&*()-_=+[]{}|;:,.<>?/' for char in password)):
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, one special character')


        self.username = username
        self.email = email
        self.password = password

    def get(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }