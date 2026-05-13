from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Firebase configuration
BASE_URL = "https://chat-app-1131410049-default-rtdb.firebaseio.com"
MESSAGES_URL = f"{BASE_URL}/messages.json"

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
        response = requests.get(MESSAGES_URL)
        data = response.json()
        return jsonify(data if data else {})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    # data should include: name, text, avatar, mood, likes
    response = requests.post(MESSAGES_URL, json=data)
    return jsonify(response.json())

@app.route('/api/like/<msg_id>', methods=['PATCH'])
def like_message(msg_id):
    url = f"{BASE_URL}/messages/{msg_id}.json"
    current = requests.get(url).json()
    new_likes = (current.get('likes', 0) if current else 0) + 1
    requests.patch(url, json={"likes": new_likes})
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
