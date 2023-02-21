#!/usr/bin/env python3
import sys
import tkinter as tk


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        cipher_text = ""

        for _ in plain_text:
            if _.isalpha():
                if _.isupper():
                    cipher_text += chr((ord(_) + self.key - 65) % 26 + 65)
                else:
                    cipher_text += chr((ord(_) + self.key - 97) % 26 + 97)
            elif _.isnumeric():
                cipher_text += chr((ord(_) + self.key - 48) % 10 + 48)
            else:
                cipher_text += _
        
        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = ""

        for _ in cipher_text:
            if _.isalpha():
                if _.isupper():
                    plain_text += chr((ord(_) - self.key - 65) % 26 + 65)
                else:
                    plain_text += chr((ord(_) - self.key - 97) % 26 + 97)
            elif _.isnumeric():
                plain_text += chr((ord(_) - self.key - 48) % 10 + 48)
            else:
                plain_text += _
        
        return plain_text

    def decrypt_bf(self, cipher_text):
        possible_text = []

        for i in self.key:
            plain_text = ""

            for _ in cipher_text:
                if _.isalpha():
                    if _.isupper():
                        plain_text += chr((ord(_) - i - 65) % 26 + 65)
                    else:
                        plain_text += chr((ord(_) - i - 97) % 26 + 97)
                elif _.isnumeric():
                    plain_text += chr((ord(_) - i - 48) % 10 + 48)
                else:
                    plain_text += _
                
            possible_text.append((plain_text, i))
        
        return possible_text


def caesar():
    options = [1, 2, 3]
    keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    try:
        user_input = input("Enter MESSAGE to encrypt/decrypt: ")
    except:
        print("An Error occurred processing input.")

    print("\nCaesar Cipher Algorithm Options:")
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
    
    if option == 1 or option == 2:
        while True:
            try:
                key = int(input("\nEnter encryption/decryption KEY value: "))
                while key not in keys:
                    key = int(input("Invalid Entry! Enter a key value between 1 and 25."))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        cipher = CaesarCipher(key)
        
        if option == 1:
            result = cipher.encrypt(user_input)
        else:
            result = cipher.decrypt(user_input)

        print(f"\nMessage: {user_input}, Key: {key}")
        print("Processing.....................")
        print(f"\n{user_input} ==> {result}")

    else:
        key = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        cipher = CaesarCipher(key)
        result = cipher.decrypt_bf(user_input)

        mid_column = max(len(str(_[0])) for _ in result)
        print(f"{'Key':<3}\t{'Text':<{mid_column}}")
        for i in range(len(result)):
            print(f"{result[i][1]:<3}\t{result[i][0]:<{mid_column}}")


'''def caesar_gui():
    root = tk.Tk()
    root.title("Caesar Cipher")

    user_entry_label = tk.Label(root, text="Plain Text: ")
    user_entry_label.grid(row=0, column=0, padx=5, pady=5)
    user_entry = tk.Entry(root)
    user_entry.grid(row=0, column=1, padx=5, pady=5)

    key_label = tk.Label(root, text="Key:")
    key_label.grid(row=1, column=0, padx=5, pady=5)
    key_entry = tk.Entry(root)
    key_entry.grid(row=1, column=1, padx=5, pady=5)

    def submit_inputs

    encrypt_button = tk.Button(root, text="Encrypt", command=caesar_encrypt_gui)
    encrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()'''


def main(argv):
    caesar()


if __name__ == "__main__":
    main(sys.argv[1:])