import crypt
from sys import argv
from cs50 import get_string

def main():

    # if the command line takes in too few or too many arguments
    if len(argv) != 2:
        exit("Usage: python crack.py hash")

    # the hash/salt is the word entered in argument
    salt = argv[1]

    # string of all guessable letters to route through
    guess = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    crack_it(guess, salt)

    exit("Password longer than 5 characters or not only alphas.")

# function to run through nested loops to actually guess/crack the password
def crack_it(guess, salt):

    for c in guess:
        # if hash of password = the command hash
        if salt == crypt.crypt(c, salt):
            exit(c)

    for c in guess:
        for d in guess:
            if salt == crypt.crypt(c + d, salt):
                exit(c + d)

    for c in guess:
        for d in guess:
            for e in guess:
                if salt == crypt.crypt(c + d + e, salt):
                    exit(c + d + e)

    for c in guess:
        print(c)
        for d in guess:
            for e in guess:
                for f in guess:
                    if salt == crypt.crypt(c + d + e + f, salt):
                        exit(c + d + e + f)

    for c in guess:
        for d in guess:
            for e in guess:
                for f in guess:
                    for g in guess:
                        if salt == crypt.crypt(c + d + e + f + g, salt):
                            exit(c + d + e + f + g)

if __name__ == "__main__":
    main()
