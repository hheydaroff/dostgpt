import config
import requests

# Load API key
perplexity_api_key = config.load_perplexity_api_key()


def chat_with_perplexity(messages, custom_prompt):


    system_message = custom_prompt + "\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    headers = {
        "Authorization": f"Bearer {perplexity_api_key}"
    }

    payload = {
        "model": "llama-2-70b-chat",
        
        "messages": [{"role": "system", "content": system_message}] + messages
    }

    response = requests.post("https://api.perplexity.ai/chat/completions", 
                            headers=headers, json=payload)

    return response.json()["choices"][0]["message"]["content"]