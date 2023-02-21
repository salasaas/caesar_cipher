#!/usr/bin/env python3
import sys


def caesar():
    options = [1, 2, 3]

    print("Caesar Cipher Algorithm Options:")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Brute Force Decoder")

    while True:
        try:
            option = int(input("\nEnter Number to Select Option: "))
            while option not in options:
                option = int(input("Invalid Entry! Enter options '1', '2', or '3': "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    if option == 1:
        caesar_encode()
    elif option == 2:
        caesar_decode()
    else:
        caesar_bf()


def caesar_encode():
    keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    cipher_text = ""

    try:
        user_input = input("\nEnter plain text string to encode: ")
    except:
        print("An Error occurred processing input.")

    while True:
        try:
            key = int(input("Enter a key value to encode: "))
            while key not in keys:
                key = int(input("Invalid Entry! Enter a key value between 1 and 25."))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f"\nPlain Text: {user_input}, Key: {key}")
    print("Processing.....................")

    for _ in user_input:
        if _.isalpha():
            if _.isupper():
                cipher_text += chr((ord(_) + key - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(_) + key - 97) % 26 + 97)
        elif _.isnumeric():
            cipher_text += chr((ord(_) + key - 48) % 10 + 48)
        else:
            cipher_text += _
    
    print(f"\n{user_input} ==> {cipher_text}")


def caesar_decode():
    keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    plain_text = ""

    try:
        cipher_text = input("\nEnter an encoded string to decode: ")
    except:
        print("An Error occurred processing input.")

    while True:
        try:
            key = int(input("Enter known key value to decode: "))
            while key not in keys:
                key = int(input("Invalid Entry! Enter a key value between 1 and 25."))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f"\nCipher Text: {cipher_text}, Key: {key}")
    print("Processing.....................")

    for _ in cipher_text:
        if _.isalpha():
            if _.isupper():
                plain_text += chr((ord(_) - key - 65) % 26 + 65)
            else:
                plain_text += chr((ord(_) - key - 97) % 26 + 97)
        elif _.isnumeric():
            plain_text += chr((ord(_) - key - 48) % 10 + 48)
        else:
            plain_text += _
    
    print(f"\n{cipher_text} ==> {plain_text}")


def caesar_bf():
    keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    possible_text = []
    

    try:
        cipher_text = input("\nEnter an encoded string to brute force: ")
    except:
        print("An Error occurred processing input.")

    for key in keys:
        plain_text = ""

        for _ in cipher_text:
            if _.isalpha():
                if _.isupper():
                    plain_text += chr((ord(_) - key - 65) % 26 + 65)
                else:
                    plain_text += chr((ord(_) - key - 97) % 26 + 97)
            elif _.isnumeric():
                plain_text += chr((ord(_) - key - 48) % 10 + 48)
            else:
                plain_text += _
            
        possible_text.append((plain_text, key))

    mid_column = max(len(str(_[0])) for _ in possible_text)
    print(f"{'Key':<3}\t{'Text':<{mid_column}}")
    for i in range(len(possible_text)):
        print(f"{possible_text[i][1]:<3}\t{possible_text[i][0]:<{mid_column}}")


def main(argv):
    caesar()


if __name__ == "__main__":
    main(sys.argv[1:])