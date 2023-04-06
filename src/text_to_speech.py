import datetime
from datetime import datetime

from gtts import gTTS


def speak(dir_output, text):
    today = datetime.now()
    tts = gTTS(text=text, lang="en")
    filename = dir_output + "/VOICE {}.mp3".format(today)
    tts.save(filename)
    print("Created : " + filename)
    print("Text    : " + text)
    print("---------------------------------------------------------------")
