from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

def get_ai_response(message):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {"role":"system","content":"You are a hacker assistant."},
            {"role":"user","content":message}
        ]
    )

    return response.choices[0].message.content