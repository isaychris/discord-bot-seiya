import random

with open('jokes.txt', encoding="utf8") as fp:
    jokes = fp.read().split("\n")

def getJoke():
    result = random.choice(jokes)
    return result
