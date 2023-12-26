from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import core
import os

app = Flask(__name__)
CORS(app)

load_dotenv()
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN')

@app.route('/webhook', methods=['GET'])
def verify_token():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge
        else:
            return "Verify token mismatch", 403
    return "Verification failed", 400

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json
    # TODO get the message from the data
    # TODO call processs message from core
    return "Success", 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
