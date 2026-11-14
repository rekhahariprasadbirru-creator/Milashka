from brain import milashka_response

print("================================")
print("       MILASHKA AI")
print("================================")

print("Hello! I am Milashka.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Milashka: Goodbye!")
        break

    response = milashka_response(user_message)
    print("Milashka:", response)
