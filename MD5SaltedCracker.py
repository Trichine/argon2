import hashlib

numbers = [f"{number:04d}" for number in range(10000)]

HASHANDSALT = input("Enter the MD5 hash you wanna crack: ").split("$")
HASH = HASHANDSALT[0]
SALT = HASHANDSALT[1]

print(HASH)
print(SALT)


def main():
    for number in numbers:
        guess = hashlib.md5(str(number + SALT).encode()).hexdigest()
        if guess == HASH:
            print(f"[+] Password found: {number}")
            exit(0)
        else:
            print(f"[-] Guess: {number} incorrect...")


main()
