from chatbot import Chatbot

chatbot = Chatbot("dataset.json")
print("🤖 Chatbot is ready! Type 'exit' to stop chatting.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)
