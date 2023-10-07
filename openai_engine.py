import openai
import config

# Load API key
openai.api_key = config.load_openai_api_key()

def chat_with_gpt3(messages, custom_prompt, model = "gpt-3.5-turbo"):
    system_message = custom_prompt + "\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    try: 
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": system_message}] + messages,
            max_tokens=1000
        )

        reply = response.choices[0].message.content

        return reply
    except Exception as e:
        print(f"An error occurred during the OpenAI API call: {str(e)}")
        return "An error occurred while generating a response."
