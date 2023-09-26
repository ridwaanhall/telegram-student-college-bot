import os
from flask import Flask, Response, request
from Controller.StudentController import ANSWERE, MESSAGE

app = Flask(__name__)
# Get BOT Token from telegram

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, incoming_que = MESSAGE.message_parser(msg)
        answer = ANSWERE.generate_answer(incoming_que)
        MESSAGE.send_message_telegram(chat_id, answer)
        return Response('ok', status=200)
    else:
        return "<h1>gew uda muakk</h1>"