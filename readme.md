# DostGPT CLI Chatbot

This is a Command-Line Interface (CLI) application for a chatbot that utilizes the OpenAI GPT model. The chatbot is designed to generate human-like responses based on the user input.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/hheydaroff/dostgpt.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dostgpt
   ```

3. Obtain an OpenAI API key and add it to the `config.ini` file. You can create an OpenAI account and generate an API key from their website.

   ```ini
   [OpenAI]
   api_key = YOUR_API_KEY
   ```

## Usage

To start the chatbot CLI, run the following command:

```bash
./run_dostgpt.sh
```

The chatbot will ask for user input and generate a response based on the provided prompt. It will continue to interact with the user until the user chooses to exit.

## Configuration

The `config.ini` file contains the configuration settings for the chatbot CLI app. You can modify the following options:

- `api_key`: Your OpenAI API key. Make sure to keep this key secure and do not share it publicly.

You can also change the LLM model of OpenAI inside the `dostgpt.py` file.

## License

This project is licensed under the [MIT License](LICENSE).
