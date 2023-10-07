# DostGPT CLI Chatbot

This is a Command-Line Interface (CLI) application for a chatbot that utilizes the OpenAI GPT model. The chatbot is designed to generate human-like responses based on user input.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/hheydaroff/dostgpt.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dostgpt
   ```

3. Obtain an OpenAI API key and add it to the `config.ini` file. If `config.ini` does not exist, create one in the same directory. You can create an OpenAI account and generate an API key from their website. Also mention which models you want to use.

```ini
[OpenAICredentials]
API_KEY = xxxxxxxxxxxxx

[PerplexityCredentials]
API_KEY = xxxxxxxxxxxxx

[PerplexityModels]
llama = llama-2-70b-chat
codellama = codellama-34b-instruct
mistral = mistral-7b-instruct

[OpenAIModels]
gpt35turbo = gpt-3.5-turbo
gpt35turbo16k = gpt-3.5-turbo-16k
```

4. Ensure you have Python 3 installed on your machine.

5. Install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the chatbot CLI, run the following command:

```bash
./run_dostgpt.sh
```

The chatbot will ask for user input and generate a response based on the provided prompt. It will continue to interact with the user until the user chooses to exit.

### Limitation
So that user can enter multiline text, every time to submit the input, user should press `Enter` at the new empty line.

### Commands

- **forget**: Clears the conversation history and starts a new conversation.
- **exit**: Shuts down the application gracefully, saving the conversation history to a text file in the 'history/' folder.
- **change engine**: Asks again which engine and models you want to use.

## Configuration

The `config.ini` file contains the configuration settings for the chatbot CLI app. You can modify the following options:
```
[OpenAICredentials]
API_KEY = xxxxxxxxxxxxx

[PerplexityCredentials]
API_KEY = xxxxxxxxxxxxx

[PerplexityModels]
llama = llama-2-70b-chat
codellama = codellama-34b-instruct
mistral = mistral-7b-instruct

[OpenAIModels]
gpt35turbo = gpt-3.5-turbo
gpt35turbo16k = gpt-3.5-turbo-16k
```

## History

The history of the chatbot's conversation is automatically saved to a text file in the 'history/' folder. You can review past conversations there.

## License

This project is licensed under the [MIT License](LICENSE).
