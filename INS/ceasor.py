import os

def caesar_encryption(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            input_text = file.read().strip()  # Read input text from file

        encrypted_text = []
        for char in input_text:
            ascii_val = ord(char)
            if 'A' <= char <= 'Z':
                encrypted_char = chr((ascii_val - ord('A') + key) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                encrypted_char = chr((ascii_val - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted_char = char
            encrypted_text.append(encrypted_char)

        with open(output_file, 'w') as file:
            file.write(''.join(encrypted_text))  # Write encrypted text to file
        print(f"File encrypted and saved to {output_file}")
        print("Encrypted content:")
        print(''.join(encrypted_text))

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def caesar_decryption(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            encrypted_text = file.read().strip()  # Read encrypted text from file

        decrypted_text = []
        for char in encrypted_text:
            ascii_val = ord(char)
            if 'A' <= char <= 'Z':
                decrypted_char = chr((ascii_val - ord('A') - key) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                decrypted_char = chr((ascii_val - ord('a') - key) % 26 + ord('a'))
            else:
                decrypted_char = char
            decrypted_text.append(decrypted_char)

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
    key = int(input("Enter the key for Caesar cipher: "))
    while True:
        choice = main_menu()
        if choice == '1':
            input_file = input("Enter the path of the input file (default: input.txt): ") or "input.txt"
            output_file = input("Enter the path where encrypted file should be stored (default: encrypted.txt): ") or "encrypted.txt"
            caesar_encryption(input_file, output_file, key)
        elif choice == '2':
            input_file = input("Enter the path of the encrypted file (default: encrypted.txt): ") or "encrypted.txt"
            output_file = input("Enter the path where decrypted file should be stored (default: decrypted.txt): ") or "decrypted.txt"
            caesar_decryption(input_file, output_file, key)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
