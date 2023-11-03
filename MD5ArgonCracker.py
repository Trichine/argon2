import hashlib
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


numbers = [f"{number:04d}" for number in range(10000)]

HASHANDSTUFF = input("Enter the MD5 hash you wanna crack: ")
# HASH = HASHANDSTUFF[4]
# SALT = HASHANDSTUFF[3]
# NAME = HASHANDSTUFF[0]
# VERSION = HASHANDSTUFF[1]
# PARAMS = HASHANDSTUFF[2].split(",")
ph = PasswordHasher()


def main():
    for number in numbers:
        try:
            guess = ph.verify(HASHANDSTUFF, number)
        except VerifyMismatchError:
            print(f"[-] Guess: {number} incorrect...")
            continue

        print(f"[+] Password found: {number}")
        exit(0)


main()
#python3 MD5ArgonCracker.py