from random import shuffle


def jumble_words(sentence: str) -> str:
    words = sentence.split()
    shuffle(words)
    return " ".join(words)
