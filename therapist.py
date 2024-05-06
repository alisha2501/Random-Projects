import random
from nltk.chat.util import Chat, reflections

# Define reflections to map first-person pronouns to second-person pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define patterns and responses for the chatbot
patterns = [
    # (r"(.*)", ("I'm here to listen. Please tell me more.",)),
    (r"(.*)help(.*)", ("You can talk to me about anything. What's on your mind?",)),
    (r"(.*)sad(.*)", ("I'm sorry to hear that you're feeling sad. Would you like to talk about why?",)),
    (r"(.*)suicide(.*)", ("GO FOR IT",)),
    (r"(.*)anxious(.*)", ("Anxiety can be tough to deal with. What's making you anxious?",)),
    (r"(.*)depressed(.*)", ("Depression is a serious issue. Have you considered seeking professional help?",)),
    (r"(.*)lonely(.*)", ("Feeling lonely can be difficult. Would you like to share why you feel this way?",)),
    (r"(.*)happy(.*)", ("It's great to hear that you're feeling happy! What's making you feel this way?",)),
    (r"(.*)quit(.*)", ("Quitting is not always the best option. Let's talk about what's bothering you.",)),
    (r"(.*)alone(.*)", ("Feeling alone can be tough. I'm here to listen if you need someone to talk to.",)),
    (r"(.*)lost(.*)", ("Feeling lost is part of the journey. Let's find your way together.",)),
    (r"(.*)stressed(.*)", ("Stress can weigh heavy, but there are ways to manage it. What's been stressing you out?",)),
    (r"(.*)confused(.*)", ("Confusion is just a temporary state. Let's clear things up together.",)),
    (r"(.*)afraid(.*)", ("Fear can hold us back, but facing it can lead to growth. What are you afraid of?",)),
    (r"(.*)angry(.*)", ("Anger is a valid emotion. Let's explore what's triggering it.",)),
    
    (r"(.*)overwhelmed(.*)", ("Feeling overwhelmed happens to the best of us. Let's break it down into manageable steps.",)),
    (r"(.*)believe(.*)", ("Believe in yourself and all you want to be. Dont let what other people say or do make you frown. Let in the good times and get through the bad. You are in the right place, and your heart is leading you on the way to great tomorrow. The longer you practice the habit of working towards your dreams, the easier the journey will become",)),
    (r"(.*)", ("I'm here to listen. Please tell me more.",))
]

# Create a chatbot with the defined patterns and reflections
chatbot = Chat(patterns, reflections)

# Define a function to start the chat
def therapist_chat():
    print("Welcome! How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Thank you for talking with me. Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print(response)

# Start the chat
therapist_chat()
