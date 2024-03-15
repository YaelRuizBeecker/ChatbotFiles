from flask import Flask,request
from flask import send_file
from helper.twilio_api import send_file_message
from helper.twilio_api import send_message

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Everything Working Fine :)</h1>"

@app.route("/getFile")
def getFile():
    return send_file(r'F:\BEECKER\SendFilesBot\videoplayback.mp3')

@app.route("/twilio/receiveMessage", methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']
        send_file_message(sender_id, 'Here is the requested info', request.base_url)
    except Exception as e:
        send_message(sender_id, 'Sorry, but we had an internal server error. Could you repeat the query')
        print(e)
        return f'Error: {e}', 500
    return 'OK', 200

app.run()