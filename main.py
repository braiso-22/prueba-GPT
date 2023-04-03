# coding=utf-8
import dotenv
from dotenv import load_dotenv
import openai

from Assistant import Assistant
from Message import Message


def fast_completion(assistant: Assistant):
    while True:
        message = input("You: ")
        if message == "":
            break
        completion = assistant.create_completion(message)
        text = completion.choices[0].text
        print(f"{assistant.name}: {text}")


def open_chat(assistant: Assistant):
    first_message = True
    while True:
        if first_message:
            option = input("Quieres configurar a tu asistente?s/N")
            message_str = input("Configuracion: ") if option.lower() == "s" else ""

            assistant.initial_configuration(message_str)
            first_message = not first_message

        message_str = input("You: ")
        if message_str == "":
            break

        message = Message("user", message_str)
        assistant.add_message(message)
        completion = assistant.send_conversation()
        text = completion.choices[0].message.content
        print(f"{assistant.name}: ")
        [print(text + "\n") for text in text.split(". ")]
        assistant.add_message(Message(Message.ASSISTANT, text))


def main():
    assistant = Assistant("Jarvis")
    menu_options = {
        "1": fast_completion,
        "2": open_chat,
    }
    while True:
        print("1. Simple question")
        print("2. Chating")
        print("0. Exit")
        option = input("Option: ")

        if option == "0":
            break
        if option in menu_options:
            menu_options[option](assistant)
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
