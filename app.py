# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# IMPORTANT: Ensure this URL matches your Firebase exactly
# It MUST end with /messages.json
FIREBASE_URL = "https://chat-app-1131410049-default-rtdb.firebaseio.com/"

@app.route('/')
def index(): return render_template('login.html')

@app.route('/board')
def board(): return render_template('board.html')

@app.route('/get_messages')
def get_messages():
    print(f"Attempting to fetch from: {FIREBASE_URL}")
    try:
        response = requests.get(FIREBASE_URL)
        data = response.json()
        print(f"Firebase Response: {data}")
        return jsonify(data if data else {})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    print(f"Sending to Firebase: {data}")
    # POST to .../messages.json creates a new entry
    response = requests.post(FIREBASE_URL, json=data)
    print(f"Post Status: {response.status_code}")
    return jsonify(response.json())

@app.route('/api/like/<msg_id>', methods=['PATCH'])
def like_message(msg_id):
    # For PATCH, we target the specific ID: .../messages/ID.json
    url = f"https://chat-app-1131410049-default-rtdb.firebaseio.com/messages/{msg_id}.json"
    current = requests.get(url).json()
    new_likes = (current.get('likes', 0) if current else 0) + 1
    requests.patch(url, json={"likes": new_likes})
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
