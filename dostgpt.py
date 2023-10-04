import openai
import configparser
import datetime
import os
import sys

# Load API key
config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = config["OpenAI"]["api_key"]

# Chatbot function using chat completions endpoint
def chat_with_gpt3(messages, custom_prompt):
    # Prepend custom prompt to messages
    system_message = custom_prompt + "\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}] + messages,
        max_tokens=1000
    )

    reply = response.choices[0].message.content

    return reply

# Function to save chat history to a text file
def save_chat_history(conversation):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"history/chat_history_{timestamp}.txt"

    os.makedirs("history", exist_ok=True)

    with open(filename, "w") as f:
        for msg in conversation:
            f.write(f"{msg['role']}: {msg['content']}\n")

    print(f"Chat history saved to {filename}")

# Main loop
print("Welcome to DostGPT!")

conversation = []

# Ask user for custom prompt initially
print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")

custom_prompt = sys.stdin.read()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        save_chat_history(conversation)
        break

    if user_input.lower() == "forget":
        save_chat_history(conversation)
        conversation = []
        print("DostGPT: Conversation history cleared.")
        print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")
        custom_prompt = sys.stdin.read()
        continue

    conversation.append({"role": "user", "content": user_input})

    reply = chat_with_gpt3(conversation, custom_prompt)

    conversation.append({"role": "assistant", "content": reply})

    print("DostGPT:", reply)
