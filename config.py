import configparser

def load_openai_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["OpenAI"]["api_key"]

def load_perplexity_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["Perplexity"]["api_key"]