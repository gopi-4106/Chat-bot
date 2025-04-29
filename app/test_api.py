import requests

# URL of your Flask API
url = "http://127.0.0.1:5000/chat"

# A single message to send (you are NOT sending the whole dataset here)
data = {
    "message": "What is Python?"
}

# Send POST request
response = requests.post(url, json=data)

# Print chatbot's response
print("Bot:", response.json()["response"])