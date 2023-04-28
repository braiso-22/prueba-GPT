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
        if type(completion) == Exception:
            print(completion)
            break
        text = completion.choices[0].message.content
        print(f"{assistant.name}: ")
        [print(text + "\n") for text in text.split(". ")]
        assistant.add_message(Message(Message.ASSISTANT, text))


def generar_imagen(assistant: Assistant):
    while True:
        message = input("You: ")
        if message == "":
            break
        image_url = assistant.generar_imagen(message)
        filename = input("Nombre de la imagen: ")
        guardar_imagen(filename, image_url)


def guardar_imagen(filename: str, image_url: str):
    import requests
    response = requests.get(image_url)
    folder = "images"
    # create folder if not exists
    import os
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(f"{folder}/{filename}.png", "wb") as file:
        file.write(response.content)
    print(f"Imagen guardada en {folder}/{filename}")


def main():
    assistant = Assistant("Jarvis")
    menu_options = {
        "1": fast_completion,
        "2": open_chat,
        "3": generar_imagen
    }
    while True:
        print("1. Simple question")
        print("2. Chating")
        print("3. Generar imagen")
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
