# part code base on https://medium.com/zenofai/creating-chatbot-using-python-flask-d6947d8ef805
# /index.py
from flask import Flask, request, jsonify, render_template
import os
import chatty

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    chatty_bot = chatty.chatty()
    fulfillment_text = chatty_bot.chat_respond(message.lower())
    response_text = { "message":  fulfillment_text }
    return jsonify(response_text)

# run Flask app
if __name__ == "__main__":
    app.run()