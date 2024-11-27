def chatbot():
    print("Welcome to the Simple Chatbot!")
    print("You can ask me the following questions:")
    print("1. Hi!")
    print("2. How are you?")
    print("3. Are you working?")
    print("4. What is your name?")
    print("5. What did you do yesterday?")
    print("Type 'exit' to end the chat.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input == "Hi!":
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input == "How are you?":
            print("Chatbot: I'm just a program, but I'm doing well! Thank you for asking.")
        elif user_input == "Are you working?":
            print("Chatbot: Yes, I'm here to chat with you!")
        elif user_input == "What is your name?":
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif user_input == "What did you do yesterday?":
            print("Chatbot: I don't have memories like humans, but I was here waiting for you!")
        else:
            print("Chatbot: I'm sorry, I don't understand that question.")

if __name__ == "__main__":
    chatbot()