from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import core
import os
import requests

app = Flask(__name__)
CORS(app)

load_dotenv()
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')
FACEBOOK_API_URL = os.getenv('FACEBOOK_API_URL')

def call_send_api(sender_id, message):
    headers = {"Content-Type": "application/json"}

    auth = {"access_token": PAGE_ACCESS_TOKEN}

    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {"id": sender_id},
        "message": {"text": message}
    }
    response = requests.post(FACEBOOK_API_URL, headers=headers, params=auth, json=payload)
    return response

@app.route('/', methods=['GET'])
def verify_token():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verify token mismatch", 403
    return "Verification failed", 400

@app.route('/', methods=['POST'])
def webhook():
    """POST endpoint to recieve messages

    Returns:
        200: OK
    """
    data = request.get_json()
    # TODO get the message from the data
    # TODO call processs message from core
    try:
        entries = data['entry']
        for entry in entries:
            message = entry['messaging'][0]['message']['text']
            sender_id = entry['messaging'][0]['sender']['id']
            core.process_message(sender_id, message)
    except Exception as e:
        # Catch all for any exceptions in core
        print(e)
    return "Success", 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
