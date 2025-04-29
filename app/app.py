from flask import Flask, request, jsonify, render_template
from chatbot import Chatbot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

chatbot = Chatbot("dataset.json")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"response": "Please provide a message."})

    response = chatbot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
