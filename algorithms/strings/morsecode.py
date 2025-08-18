from functools import reduce

morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

inverseAlphabet = reduce(
    lambda a, b: dict(list(a.items()) + list(b.items())),
    [{morseAlphabet[k]: k} for k in morseAlphabet.keys()],
    {},
)


def encode(_text):
    return " ".join([morseAlphabet[_c.upper()] for _c in _text[:]])


def decode(_text):
    return "".join([inverseAlphabet[_c] for _c in _text.split(" ")])


def test():
    print(decode(encode("TEST")) == "TEST")


if __name__ == "__main__":
    test()
