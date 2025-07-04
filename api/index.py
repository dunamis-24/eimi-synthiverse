from flask import Flask, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=['POST'])
def chat():
    user_input = request.json.get('prompt')
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful chatbot."},
            {"role": "user", "content": user_input}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    app.run()
