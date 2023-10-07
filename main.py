# main.py

import utils
import history

# Introduction and guidelines for users
print("Welcome to DostGPT!")
print("DostGPT is a conversational AI that can assist you with various tasks.")
print("You can interact with DostGPT by typing your messages, and you can use the following commands:")
print("- 'quit', 'exit', or 'end conversation' to gracefully exit the program.")
print("- 'forget' to clear the conversation history and start a new conversation.")
print("- 'change engine' to switch between AI engines.")
print("Let's get started!")


conversation_history = []  # Stores the conversation history
config = utils.read_configuration()

def main():
    while True:
        utils.print_divider()
        engine_choice, model = utils.choose_engine_and_model(config)  # Pass the config object here
    
        # Clear conversation history and reset the custom prompt if the user chooses a new engine
        utils.clear_conversation(conversation_history)
        custom_prompt = utils.get_user_input("Enter prompt for how the DostGPT should respond. Press Enter on an empty line when done:")

        while True:
            utils.print_divider()
            print("Write your message. Press Enter on an empty line when done:")
            user_input_message = utils.get_user_input("You: ")

            if user_input_message.lower() in ["exit", "quit", "end conversation"]:
                utils.save_chat_history(conversation_history)
                exit()

            if user_input_message.lower() == "forget":
                utils.save_chat_history(conversation_history)
                utils.clear_conversation(conversation_history)
                custom_prompt = utils.get_user_input("Enter prompt for how the DostGPT should respond. Press Enter on an empty line when done:")
                continue

            if user_input_message.lower() == "change engine":
                utils.clear_conversation(conversation_history)  
                break

            conversation_history.append({"role": "user", "content": user_input_message})
            response = utils.get_response(engine_choice, model, conversation_history, custom_prompt)
            conversation_history.append({"role": "assistant", "content": response})

            # Print the user input, assistant's reply, and a divider
            print("You:", user_input_message)
            utils.print_divider()
            print("DostGPT:", response)

if __name__ == "__main__":
    main()
