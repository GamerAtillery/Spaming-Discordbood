import random
from typing import Mapping
messages = [
    "test",
    "test2",
    "testmessage",
    "floh: 'Was ist eine spalte?'"
]


def getRandomMessage():
    return random.choice(messages)


if __name__ == "__main__":
    print(getRandomMessage())