import sys
import openai_engine
import perplexity_engine
import config
import history

print("Welcome to DostGPT!")

conversation = []

# Ask user for custom prompt initially
engine_choice = input("Would you like to talk with OpenAI (openai) or Perplexity (perplexity) : ")
print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")

custom_prompt = sys.stdin.read()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        history.save_chat_history(conversation)
        break

    if user_input.lower() == "forget":
        history.save_chat_history(conversation)
        conversation = []
        print("DostGPT: Conversation history cleared.")
        print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")
        custom_prompt = sys.stdin.read()
        continue
    
    if user_input.lower() == "change engine":
        history.save_chat_history(conversation)
        conversation = []
        print("DostGPT: Conversation history cleared.")
        engine_choice = input("Would you like to talk with OpenAI (openai) or Perplexity (perplexity) : ")
        print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")
        custom_prompt = sys.stdin.read()
        continue

    conversation.append({"role": "user", "content": user_input})
    
    if engine_choice == "openai":
        reply = openai_engine.chat_with_gpt3(conversation, custom_prompt)
    elif engine_choice == "perplexity":
        reply = perplexity_engine.chat_with_perplexity(conversation, custom_prompt)
        
        

    conversation.append({"role": "assistant", "content": reply})

    print("DostGPT:", reply)
