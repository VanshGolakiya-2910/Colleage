import string
import random
import os

def generate_key():
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    key = []
    
    while lowercase_letters:
        random_letter_lower = random.choice(lowercase_letters)
        random_letter_upper = random.choice(uppercase_letters)
        temp = {random_letter_lower: random_letter_upper}
        key.append(temp)
        lowercase_letters.remove(random_letter_lower)
        uppercase_letters.remove(random_letter_upper)
    
    return key

def find_value_for_lowercase(letter, key):
    for item in key:
        if letter in item:
            return item[letter]
    return letter  # Return the original letter if not found in key

def find_key_for_value(value, key):
    for item in key:
        for k, v in item.items():
            if v == value:
                return k
    return value  # Return the original value if not found in key

def encryption(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            text = file.read().strip()  # Read input text from file
        
        if not text:
            print(f"The input file '{input_file}' is empty. Please provide text in the file to encrypt.")
            return
        
        encrypted_text = []
        for char in text:
            if char.islower():
                encrypted_text.append(find_value_for_lowercase(char, key))
            elif char.isupper():
                encrypted_text.append(find_key_for_value(char, key))
            else:
                encrypted_text.append(char)
        
        with open(output_file, 'w') as file:
            file.write(''.join(encrypted_text))  # Write encrypted text to file
        print(f"File encrypted and saved to {output_file}")
        print("Encrypted content:")
        print(''.join(encrypted_text))

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decryption(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            encrypted_text = file.read().strip()  # Read encrypted text from file
        
        if not encrypted_text:
            print(f"The encrypted file '{input_file}' is empty. Please provide text in the file to decrypt.")
            return
        
        decrypted_text = []
        for char in encrypted_text:
            if char.islower():
                decrypted_text.append(find_value_for_lowercase(char, key))
            elif char.isupper():
                decrypted_text.append(find_key_for_value(char, key))
            else:
                decrypted_text.append(char)
        
        with open(output_file, 'w') as file:
            file.write(''.join(decrypted_text))  # Write decrypted text to file
        print(f"File decrypted and saved to {output_file}")
        print("Decrypted content:")
        print(''.join(decrypted_text))

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def main_menu():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    key = generate_key()
    while True:
        
        choice = main_menu()
        
        if choice == '1':
            input_file = input("Enter the path of the input file (default: D:\\ET22BTCO039\\monoalpha\\input.txt): ") or "D:\\ET22BTCO039\\monoalpha\\input.txt"
            output_file = input("Enter the path where encrypted file should be stored (default: D:\\ET22BTCO039\\monoalpha\\encrypted.txt): ") or "D:\\ET22BTCO039\\monoalpha\\encrypted.txt"
            encryption(input_file, output_file, key)
        
        elif choice == '2':
            input_file = input("Enter the path of the encrypted file (default: D:\\ET22BTCO039\\monoalpha\\encrypted.txt): ") or "D:\\ET22BTCO039\\monoalpha\\encrypted.txt"
            output_file = input("Enter the path where decrypted file should be stored (default: D:\\ET22BTCO039\\monoalpha\\decrypted.txt): ") or "D:\\ET22BTCO039\\monoalpha\\decrypted.txt"
            decryption(input_file, output_file, key)
        
        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
