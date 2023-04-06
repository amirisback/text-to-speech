import os

from src.text_to_speech import speak

# Directory
dir_output = "output"


def create_folder_output():
    # Path
    path = os.path.join(dir_output)

    try:
        os.makedirs(path, exist_ok=True)
        print("Directory '%s' created successfully" % dir_output)
        print("---------------------------------------------------------------")
    except OSError as error:
        print("Directory '%s' can not be created" % dir_output)
        print("---------------------------------------------------------------")


def welcome_message():
    print("---------------------------------------------------------------")
    print("TEXT TO SPEECH")
    print("Design By : M. Faisal Amir")
    print("Github    : www.github.com/amirisback")
    print("---------------------------------------------------------------")


def generate_speak(text):
    speak(dir_output, text)


def create_audio():
    generate_speak("Hi")
    generate_speak("Hello")
    generate_speak("How Are You?")
    generate_speak("Can I Help You?")


def main():
    welcome_message()
    create_folder_output()
    create_audio()


if __name__ == "__main__":
    main()
