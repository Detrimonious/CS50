from cs50 import get_string
from sys import argv


def main():

    # if command line takes in too few or too many arguments
    if len(argv) != 2:
        exit("Usage: python bleep.py dictionary")

    # use a set (unique values) for the dictionary. empty set
    dictionary = set()

    # take in argument which is a list of banned words, and read it. add each word to the set dictionary.
    file = open(argv[1], "r")
    for word in file:
        dictionary.add(word.rstrip("\n"))
    file.close()

    # get a string sentence from input
    message = get_string("What message would you like to censor?\n")

    # creates a list called 'sentence' that takes the entered message and splits it by spaces
    sentence = message.split()

    # for each word (text) in the sentence list, turn to lowercase. if the text is in the dictionary set, change it to *. else print the uncensored word.
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
