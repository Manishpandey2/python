import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
# model = "models/gemini-3.6-flash"
chat = client.chats.create(
    model = "models/gemini-3.6-flash"
)
# conversation = []
while True:
    content = input("You: ")
    if content.strip() == "exit":
        print("Goodbye!")
        break
    if content.strip() == "":
        print("Please ask something.")
        continue
    # conversation.append(
    #     {
    #         "role": "user",
    #         "content": content
    #     }
    # )
    # response = client.models.generate_content(
    #     model = model,
    #     contents = conversation
    # )
    response = chat.send_message(content)

    print(f"AI: {response.text}")

    # conversation.append(
    #     {
    #         "role": "model",
    #         "content": response.text
    #     }
    # )
