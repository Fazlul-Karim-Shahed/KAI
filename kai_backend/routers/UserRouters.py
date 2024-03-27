


from flask import Blueprint, request, render_template
import asyncio
from controllers.user_controllers.signup import signup

userRouter = Blueprint('userRouter', __name__)

@userRouter.route('/api/user/signup', methods=["POST"])
async def signup_fun():
    return await signup()