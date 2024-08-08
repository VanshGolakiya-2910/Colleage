import os

def vigenere_encryption(keyword, input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            input_text = file.read().strip()
    except Exception as E:
        print("Not able to read input file.")
        return

    encrypted_list = []
    key_list, n = list(keyword), len(keyword)
    j = 0  # j: key iterator

    for i in input_text:
        if i.isalpha():
            ascii_val = ord(i.lower()) - 97
            key_ascii = ord(key_list[j].lower()) - 97
            encrypted_letter = chr(((ascii_val + key_ascii) % 26) + 97)
            encrypted_list.append(encrypted_letter)
            j = (j + 1) % n
        elif i.isdigit():
            encrypted_list.append(i)
        else:
            encrypted_list.append("")  # Keep non-alphabetic characters unchanged

    encrypted_text = ''.join(encrypted_list)
    try:
        with open(output_file, 'w') as file:
            file.write(encrypted_text)
    except Exception as E:
        print("Not able to write to output file.")
        return

    print(f"File encrypted and saved to {output_file}")
    print(encrypted_text)

def vigenere_decryption(keyword, input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            input_text = file.read().strip()
    except Exception as E:
        print("Not able to read encrypted file.")
        return

    decrypted_list = []
    key_list, n = list(keyword), len(keyword)
    j = 0  # j: key iterator

    for i in input_text:
        if i.isalpha():
            ascii_val = ord(i.lower()) - 97
            key_ascii = ord(key_list[j].lower()) - 97
            decrypted_letter = chr(((ascii_val - key_ascii) % 26) + 97)
            decrypted_list.append(decrypted_letter)
            j = (j + 1) % n
        elif i.isdigit():
            decrypted_list.append(i)
        else:
            decrypted_list.append("")  # Keep non-alphabetic characters unchanged

    decrypted_text = ''.join(decrypted_list)
    try:
        with open(output_file, 'w') as file:
            file.write(decrypted_text)
    except Exception as E:
        print("Not able to write to output file.")
        return

    print(f"File decrypted and saved to {output_file}")
    print(decrypted_text)

def main_menu():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    keyword = input("Enter the keyword for Vigenère cipher: ").strip()
    while True:
        choice = main_menu()
        if choice == '1':
            input_file = input("Enter the path of the input file (default: input.txt): ") or "input.txt"
            output_file = input("Enter the path where encrypted file should be stored (default: encrypted.txt): ") or "encrypted.txt"
            vigenere_encryption(keyword, input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the path of the encrypted file (default: encrypted.txt): ") or "encrypted.txt"
            output_file = input("Enter the path where decrypted file should be stored (default: decrypted.txt): ") or "decrypted.txt"
            vigenere_decryption(keyword, input_file, output_file)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
