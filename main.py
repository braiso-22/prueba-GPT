# coding=utf-8
import dotenv
from dotenv import load_dotenv
import openai


def initialize_openai():
    openai.organization = "org-90nlZdVZc1Zg3BvFf3xIVfmD"
    openai.api_key = dotenv.get_key(".env", "OPENAI_API_KEY")
    print("OpenAI API Key:", openai.api_key)


def create_completion(prompt: str):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
    )
    return completion


def main():
    initialize_openai()
    while True:
        prompt = input("You: ")
        if prompt == "":
            break
        completion = create_completion(prompt)
        print("AI:", completion.choices[0].text)


if __name__ == '__main__':
    main()
