import random

# Define some possible user inputs and corresponding chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi! How can I help you?"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm fine, thanks!", "I'm doing great, thanks!"],
    "what's your name": ["My name is Chatbot. Nice to meet you!", "I'm Chatbot. What's yours?", "I'm Chatbot! How can I assist you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
}

# Define a function to generate a chatbot response based on user input
def chatbot_response(user_input):
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "Sorry, I don't understand. Could you please try again?"

# Run the chatbot
print("Welcome to Chatbot! How can I assist you?")
while True:
    user_input = input().lower()
    if user_input == "quit":
        break
    else:
        response = chatbot_response(user_input)
        print(response)