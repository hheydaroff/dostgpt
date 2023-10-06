import os
import datetime

def save_chat_history(conversation):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"history/chat_history_{timestamp}.txt"

    os.makedirs("history", exist_ok=True)

    with open(filename, "w") as f:
        for msg in conversation:
            f.write(f"{msg['role']}: {msg['content']}\n")

    print(f"Chat history saved to {filename}")