from cs50 import get_string
from sys import argv


def main():

    # TODO
    if len(argv) != 2:
        exit("Usage: python bleep.py dictionary")

    dictionary = set()

    file = open(argv[1], "r")
    for word in file:
        dictionary.add(word.rstrip("\n"))
    file.close()

    message = get_string("What message would you like to censor?\n")

    # creates a list called 'sentence' that takes the entered message and splits it by spaces
    sentence = message.split()

    for text in sentence:
        if text.lower() in dictionary:
            for c in text:
                print("*", end = "")
            print(" ", end = "")
        else:
            print(text, end = " ")

    print()


if __name__ == "__main__":
    main()
