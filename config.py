import configparser

def load_openai_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["OpenAICredentials"]["api_key"]

def load_perplexity_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["PerplexityCredentials"]["api_key"]