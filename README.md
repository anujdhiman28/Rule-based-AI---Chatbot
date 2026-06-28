#  Rule-Based Chatbot using Python

A simple command-line chatbot built with Python that uses **rule-based keyword matching** to identify user intents and respond with predefined messages. This project demonstrates basic Natural Language Processing (NLP) concepts such as text preprocessing and intent recognition without using machine learning.

##  Features

* Keyword-based intent recognition
* Text preprocessing (lowercase, whitespace, punctuation removal)
* Handles greetings, farewells, thanks, help, weather, and time queries
* Interactive command-line interface
* Easy to customize by adding new intents and responses
* No external libraries required

##  Technologies Used

* Python 3.x
* `re` (Regular Expressions)

##  Project Structure

```text
RuleBasedChatbot/
│── chatbot.py
│── README.md
```

##  Getting Started

### Prerequisites

* Python 3.x installed

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/RuleBasedChatbot.git
```

2. Navigate to the project folder:

```bash
cd RuleBasedChatbot
```

3. Run the chatbot:

```bash
python chatbot.py
```

## 💬 Example

```text
Chatbot started. Type 'exit' or 'quit' to end.

> hi
Hello! How can I help you today?

> help
I can answer simple questions and chat with you. Try asking about the weather or saying hello.

> thanks
You're welcome! If you need anything else, just ask.

> bye
Goodbye! Have a great day.
```

##  Supported Intents

| Intent   | Keywords                 |
| -------- | ------------------------ |
| Greeting | hello, hi, hey           |
| Goodbye  | bye, goodbye, quit, exit |
| Thanks   | thanks, thank you, thx   |
| Help     | help, support, assist    |
| Weather  | weather, forecast, rain  |
| Time     | time, clock              |

##  Future Improvements

* Add GUI using Tkinter
* Integrate speech recognition
* Use APIs for real-time weather and time
* Add conversation history
* Implement fuzzy matching and NLP techniques
* Upgrade to a machine learning-based chatbot

##  Author

**Anuj**
