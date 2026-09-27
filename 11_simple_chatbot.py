question = input("Ask something: ").lower()

if "hello" in question:
    print("AI: Hello! How can I help you?")
elif "name" in question:
    print("AI: I am a simple Python chatbot.")
elif "bye" in question:
    print("AI: Goodbye!")
else:
    print("AI: Sorry, I don't understand.")