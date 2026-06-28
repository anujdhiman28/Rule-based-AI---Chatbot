import re
def sanitize(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

knowledge_base = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "response": "Hello! How can I help you today?"
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "farewell", "quit", "exit"],
        "response": "Goodbye! Have a great day."
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx", "appreciate"],
        "response": "You're welcome! If you need anything else, just ask."
    },
    "help": {
        "keywords": ["help", "support", "assist", "what can you do"],
        "response": "I can answer simple questions and chat with you. Try asking about the weather or saying hello."
    },
    "weather": {
        "keywords": ["weather", "forecast", "rain", "sunny", "temperature"],
        "response": "I can't check real weather, but I hope it's nice where you are."
    },
    "time": {
        "keywords": ["time", "clock", "what time"],
        "response": "I don't have a real clock, but it's always a good time to code."
    }
}

def find_intent(user_input):
    for intent, data in knowledge_base.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return intent
    return None

def main():
    print("Chatbot started. Type 'exit' or 'quit' to end.")
    while True:
        user_input = input("> ")
        cleaned = sanitize(user_input)
        if not cleaned:
            print("Please type something.")
            continue

        intent = find_intent(cleaned)
        if intent == "goodbye":
            print(knowledge_base[intent]["response"])
            break
        if intent:
            print(knowledge_base[intent]["response"])
        else:
            print("Sorry, I don't understand that. Can you try another question?")

if __name__ == "__main__":
    main()
    # no additional code needed
