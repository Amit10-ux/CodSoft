import random

# Define intents and responses
intents = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "name": ["I'm your simple chatbot!", "You can call me CodBot."],
    "joke": ["Why don’t scientists trust atoms? Because they make up everything!",
             "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats."]
}

# Function to get response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(intents["greeting"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(intents["goodbye"])
    elif "thank" in user_input:
        return random.choice(intents["thanks"])
    elif "your name" in user_input:
        return random.choice(intents["name"])
    elif "joke" in user_input:
        return random.choice(intents["joke"])
    else:
        return "Sorry, I don’t understand that. Can you rephrase?"

# Chat loop
print("CodBot is online! Type 'quit' to exit.")
while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        print("CodBot: Goodbye!")
        break
    response = chatbot_response(user_message)
    print("CodBot:", response)
