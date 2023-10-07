# utils.py
import datetime
import os
import openai_engine
import perplexity_engine
import configparser


def save_chat_history(conversation):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"history/chat_history_{timestamp}.txt"

    os.makedirs("history", exist_ok=True)

    with open(filename, "w") as f:
        for msg in conversation:
            f.write(f"{msg['role']}: {msg['content']}\n")

    print(f"Chat history saved to {filename}")


def get_user_input(prompt):
    """Get user input until an empty line is entered."""
    user_input_lines = []
    while True:
        line = input(prompt)
        if not line:
            break
        user_input_lines.append(line)
    return '\n'.join(user_input_lines)

def print_divider():
    """Print a horizontal line to visually separate conversation parts."""
    print("-" * 40)

def clear_conversation(conversation):
    """Clear the conversation history."""
    conversation.clear()

def get_response(engine_choice, model, conversation, custom_prompt):
    """Get a response from the selected engine and model."""
    if engine_choice == "openai":
        return openai_engine.chat_with_gpt3(conversation, custom_prompt, model=model)
    elif engine_choice == "perplexity":
        return perplexity_engine.chat_with_perplexity(conversation, custom_prompt, model=model)

def read_configuration():
    """Read the configuration from the config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def choose_engine_and_model(config):
    """Ask the user to choose an engine and model."""
    while True:
        print_divider()
        engine_choice = input("Would you like to talk with OpenAI (openai) or Perplexity (perplexity): ")
    
        if engine_choice not in ["openai", "perplexity"]:
            print("Invalid choice. Please select 'openai' or 'perplexity'.")
            continue

        if engine_choice == "perplexity":
            perplexity_models_section = config['PerplexityModels']
            print("Available Perplexity Models:")
            for model_name in perplexity_models_section:
                print(f"- {model_name}")

            # Ask for the specific Perplexity model
            perplexity_model_entry = input("Enter the name of the Perplexity model you want to use: ")

            if perplexity_model_entry in perplexity_models_section:
                perplexity_model = perplexity_models_section[perplexity_model_entry]
            else:
                print("Invalid model name. Using default.")

        elif engine_choice == "openai":
            openai_models_section = config['OpenAIModels']
            print("Available OpenAI Models:")
            for model_name in openai_models_section:
                print(f"- {model_name}")

            # Ask for the specific OpenAI model
            openai_model_entry = input("Enter the name of the OpenAI model you want to use: ")

            if openai_model_entry in openai_models_section:
                openai_model = openai_models_section[openai_model_entry]
            else:
                print("Invalid model name. Using default.")

        return engine_choice, perplexity_model if engine_choice == "perplexity" else openai_model
