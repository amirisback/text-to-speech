import datetime
import os

from gtts import gTTS
from datetime import datetime

# Directory
dir_output = "output"
# Path
path = os.path.join(dir_output)

try:
    os.makedirs(path, exist_ok=True)
    print("Directory '%s' created successfully" % dir_output)
except OSError as error:
    print("Directory '%s' can not be created" % dir_output)


def speak(text):
    today = datetime.now()
    tts = gTTS(text=text, lang="en")
    filename = dir_output + "/VOICE {}.mp3".format(today)
    tts.save(filename)


speak("Hi")
speak("Hello")
speak("How Are You?")
speak("Can I Help You?")
