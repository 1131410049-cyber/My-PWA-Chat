from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# CRITICAL FIX: The URL must include "messages.json" for Firebase REST API to work
FIREBASE_URL = "https://chat-app-1131410049-default-rtdb.firebaseio.com/"

@app.route('/')
def index(): 
    return render_template('login.html')

@app.route('/board')
def board(): 
    return render_template('board.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/get_messages')
def get_messages():
    try:
        # Fetching from the corrected URL
        response = requests.get(FIREBASE_URL)
        data = response.json()
        return jsonify(data if data else {})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    # POSTing to the corrected URL
    response = requests.post(FIREBASE_URL, json=data)
    return jsonify(response.json())

@app.route('/api/like/<msg_id>', methods=['PATCH'])
def like_message(msg_id):
    # Target the specific message ID for patching likes
    url = f"https://chat-app-1131410049-default-rtdb.firebaseio.com/messages/{msg_id}.json"
    current = requests.get(url).json()
    new_likes = (current.get('likes', 0) if current else 0) + 1
    requests.patch(url, json={"likes": new_likes})
    return jsonify({"status": "ok"})

# COMBINED MAIN BLOCK: This works for both Local testing and Render deployment
if __name__ == '__main__':
    # Render uses the PORT environment variable; local uses 5000
    port = int(os.environ.get("PORT", 5000))
    # Set debug=False for production deployment (Render)
    app.run(host='0.0.0.0', port=port, debug=False)
