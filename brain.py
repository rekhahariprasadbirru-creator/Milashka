def milashka_response(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hello! I am Milashka. How can I help you?"

    elif "your name" in message:
        return "My name is Milashka."

    elif "how are you" in message:
        return "I am doing great! Thank you for asking."

    elif "who created you" in message:
        return "I was created by my developer."

    elif "bye" in message:
        return "Goodbye! See you again."

    else:
        return "I don't know that yet. I am still learning!"


