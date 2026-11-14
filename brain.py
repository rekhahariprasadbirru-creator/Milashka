
def milashka_response(message):

    message = message.lower()

    if "hello" in message:
        return "Hello! I am Milashka."

    elif "your name" in message:
        return "My name is MIlashka."

    elif "how are you" in message:
        return "I am functioning perfectly!"

    else:
        return "I am still learning. Please teach me!"


