#!/usr/bin/env python3
import sys
import tkinter as tk


class CaesarCipher:
    def __init__(self, key):
        self.key = key
        #self.keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

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


def caesar():
    keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    options = [1, 2, 3]

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
    
    if option == 1 or 2:
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
    else:
        caesar_bf()
    
    print(f"\nMessage: {user_input}, Key: {key}")
    print("Processing.....................")
    print(f"\n{user_input} ==> {result}")


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