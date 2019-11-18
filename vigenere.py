from sys import argv
from cs50 import get_string

# main function
def main():
    # if there are not two arguments, exit and return exit code 1
    if len(argv) != 2:
        exit("Usage: python vigenere.py k")

    # if the second argument for shifting key is not numeric only, exit
    else:
        for c in argv[1]:
            if c.isalpha()==0:
                exit("Usage: python vigenere.py k")

    # get the plaintext string from user, prepare the ciphertext
    plaintext = get_string("plaintext: ")
    print("ciphertext: ", end="")

    # empty list to take in the vigenere keys, numeric
    keys = []

    # for each character in the vigenere key, shift it into a number - ASCII, then add to the list of keys
    for c in argv[1]:
        keys.append(shift(c))

    # use listof keys and the inputted plaintext string, then cipher it and print newline
    plain_to_cipher(keys, plaintext)
    print()

# function to change vigenere key character-by-character into a number, which is uppercase ASCII - 65, setting 'A' to 0
def shift(character):
    character = character.upper();
    keyshift = ord(character) - 65;
    return keyshift;

# function to create ciphertext from plaintext
def plain_to_cipher(keys, plaintext):

    # to keep track of which key we are on in the vigenere key
    counter = 0;

    # for each character in the plaintext
    for d in plaintext:

        # if it is alphabetical, continue, else just print it out--a digit or space
        if (d.isupper() or d.islower()):

            # if character is uppercase. if higher than 'Z', loop down. then shift
            # ord to change char to int. chr to change int to char. ASCII
            if d.isupper():
                if ord(d) + (keys[counter] % 26) > 90:
                    d = chr(ord(d) - 26)
                d = chr(ord(d) + (keys[counter] % 26))

            # if character is lowercase. if higher than 'z', loop down. then shift
            elif d.islower():
                if ord(d) + (keys[counter] % 26) > 122:
                    d = chr(ord(d) - 26)
                d = chr(ord(d) + (keys[counter] % 26))

            # run through the counter of the vigenere key, or reset to beginning of key
            if counter < (len(argv[1])-1):
                counter += 1
            else:
                counter = 0

        # print the changed character or non-alpha character, which is generally spaces
        print(d, end="")

if __name__ == "__main__":
    main()
