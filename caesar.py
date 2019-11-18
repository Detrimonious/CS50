from sys import argv
from cs50 import get_string

# main function
def main():
    # if there are not two arguments, exit and return exit code 1
    if len(argv) != 2:
        exit("Usage: python ./caesar k")

    # if the second argument for shifting key is not numeric only, exit; else take it as the shifting key
    else:
        for c in argv[1]:
            if c.isdigit()==0:
                exit("Usage: python ./caesar k")
        shift = int(argv[1])

    # get the plaintext string from user, prepare the ciphertext, and print newline at the end
    plaintext = get_string("plaintext: ")
    print("ciphertext: ", end="")
    plain_to_cipher(shift, plaintext)
    print()

# function to create ciphertext from plaintext
def plain_to_cipher(shift, plaintext):

    # for each character in the plaintext
    for d in plaintext:

        # if character is uppercase. if higher than 'Z', loop down. then shift
        # ord to change char to int. chr to change int to char. ASCII
        if d.isupper():
            if ord(d) + (shift % 26) > 90:
                d = chr(ord(d) - 26)
            d = chr(ord(d) + (shift % 26))

        # if character is lowercase. if higher than 'z', loop down. then shift
        elif d.islower():
            if ord(d) + (shift % 26) > 122:
                d = chr(ord(d) - 26)
            d = chr(ord(d) + (shift % 26))

        # print the changed character
        print(d, end="")

if __name__ == "__main__":
    main()
