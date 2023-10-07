import sys
import openai_engine
import perplexity_engine
import config
import history

print("Welcome to DostGPT!")

conversation = []

# Ask user for custom prompt initially
engine_choice = input("Would you like to talk with OpenAI (openai) or Perplexity (perplexity) : ")
if engine_choice == "perplexity":
    perplexity_model_entry = input("Would you like to talk with llama-2(llama), codellama(codellama), or mistral(mistral): ")
print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")

custom_prompt = sys.stdin.read()

while True:
    print("Write your message. Press CTRL+D when done:")

    user_input = sys.stdin.read()

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
        if engine_choice == "perplexity":
            perplexity_model_entry = input("Would you like to talk with llama-2(llama), codellama(codellama), or mistral(mistral): ")
        print("Enter prompt for how the DostGPT should respond. Press CTRL+D when done:")
        custom_prompt = sys.stdin.read()
        continue

    conversation.append({"role": "user", "content": user_input})
    
    if engine_choice == "openai":
        reply = openai_engine.chat_with_gpt3(conversation, custom_prompt)
    elif engine_choice == "perplexity":
        if perplexity_model_entry == "llama":
            perplexity_model = "llama-2-70b-chat"
        elif perplexity_model_entry == "llamacode":
            perplexity_model = "codellama-34b-instruct"
        elif perplexity_model_entry == "mistral":
            perplexity_model = "mistral-7b-instruct"
             

        
        reply = perplexity_engine.chat_with_perplexity(conversation, custom_prompt, model = perplexity_model)
        
        

    conversation.append({"role": "assistant", "content": reply})

    print("DostGPT:", reply)
