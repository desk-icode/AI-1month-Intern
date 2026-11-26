import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

print("=" * 50)


print("       GOOGLE GEMINI AI APPLICATION")
print("=" * 50)

while True:

    question = input("\nEnter your question: ")

    if question.lower() == "exit":
        print("Application closed.")
        break

    data = {
        "contents": [
            {"parts": [{"text": question}]}
        ]
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            answer = result["candidates"][0]["content"]["parts"][0]["text"]

            print("\nGemini AI:")
            print(answer)

        else:

            print("\nAPI Error:")
            print(response.text)

    except requests.exceptions.RequestException as error:

        print("Error:", error)