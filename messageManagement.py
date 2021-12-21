import random
from typing import Mapping
messages = [
    "hallo &&name, bist du eigendlich dumm?",
    "ich bin Chris, und ich kann dich nicht leiden! &&name, das ist doch kein richtiger name",
    "testmessage",
    "https://www.youtube.com/watch?v=nOKHlWAp4No&ab_channel=unkyjayjay",
    "floh: 'Was ist eine spalte?'",
]


def getRandomMessage(name:str):
    message = random.choice(messages)
    message.replace("&&name", name)
    return message


if __name__ == "__main__":
    for i in range(5):
        print(getRandomMessage("Niklas"))