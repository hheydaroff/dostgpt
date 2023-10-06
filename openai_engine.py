import openai
import config

# Load API key
openai.api_key = config.load_openai_api_key()

def chat_with_gpt3(messages, custom_prompt):
    system_message = custom_prompt + "\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}] + messages,
        max_tokens=1000
    )

    reply = response.choices[0].message.content

    return reply