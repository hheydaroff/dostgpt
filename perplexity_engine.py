import config
import requests

# Load API key
perplexity_api_key = config.load_perplexity_api_key()


def chat_with_perplexity(messages, custom_prompt, model = 'llama-2-70b-chat'):


    system_message = custom_prompt + "\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    
    try: 
        headers = {
            "Authorization": f"Bearer {perplexity_api_key}"
        }

        payload = {
            "model": model,
            
            "messages": [{"role": "system", "content": system_message}] + messages
        }

        response = requests.post("https://api.perplexity.ai/chat/completions", 
                                headers=headers, json=payload)

        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"An error occurred during the Perplexity API call: {str(e)}")
        return "An error occurred while generating a response."