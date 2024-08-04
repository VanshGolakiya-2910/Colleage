import string
import os

def create_matrix(keyword):
    letter = list(string.ascii_lowercase)
    letter_keyword = [(i, "") for i in keyword]
    letter_keyword = list(dict(letter_keyword).keys())
    for i in letter_keyword:
        letter.remove(i)
        if i == "i":
            letter.remove('j')
    for i in letter:
        if i == "i":
            letter.remove('j')
    raw_matrix = []
    for i in letter_keyword:
        if i == "i":
            raw_matrix.append(["i", "j"])
        else:
            raw_matrix.append(i)
    for i in letter:
        if i == "i":
            raw_matrix.append(["i", "j"])
        else:
            raw_matrix.append(i)
    final_list = []
    for i in range(0, len(raw_matrix), 5):
        sublist = raw_matrix[i:i + 5]
        final_list.append(sublist)
    print("final matrix:", final_list)
    return final_list

def after_split(text):
    text = list(text)
    final_text = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            final_text.append([text[i], 'x'])
            i += 1
        elif i + 1 < len(text):
            final_text.append([text[i], text[i + 1]])
            i += 2
        else:
            final_text.append([text[i], 'x'])
            i += 1
    print("splitted text:", final_text)
    return final_text

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if char in matrix[row][col]:
                return row, col
    return None, None

def encryption(matrix, pairs):
    encrypted_text = []
    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        if r1 == r2:
            encrypted_text.append(matrix[r1][(c1 + 1) % 5])
            encrypted_text.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            encrypted_text.append(matrix[(r1 + 1) % 5][c1])
            encrypted_text.append(matrix[(r2 + 1) % 5][c2])
        else:
            encrypted_text.append(matrix[r1][c2])
            encrypted_text.append(matrix[r2][c1])
    encrypted_text = ''.join(encrypted_text)
    print("encrypted text:", encrypted_text)
    return encrypted_text

def decryption(matrix, pairs):
    decrypted_text = []
    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        if r1 == r2:
            decrypted_text.append(matrix[r1][(c1 - 1) % 5])
            decrypted_text.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:
            decrypted_text.append(matrix[(r1 - 1) % 5][c1])
            decrypted_text.append(matrix[(r2 - 1) % 5][c2])
        else:
            decrypted_text.append(matrix[r1][c2])
            decrypted_text.append(matrix[r2][c1])
    decrypted_text = ''.join(decrypted_text)
    print("decrypted text:", decrypted_text)
    return decrypted_text

def main_menu():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    keyword = input("Enter the keyword: ").replace('j', 'i')
    matrix = create_matrix(keyword)
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            input_file = input("Enter the path of the input file (default: D:\\ET22BTCO039\\playfair\\input.txt): ") or "D:\\ET22BTCO039\\playfair\\input.txt"
            output_file = input("Enter the path where encrypted file should be stored (default: D:\\ET22BTCO039\\playfair\\encrypted.txt): ") or "D:\\ET22BTCO039\\playfair\\encrypted.txt"
            try:
                with open(input_file, 'r') as file:
                    text = file.read().strip().replace('j', 'i')
                pairs = after_split(text)
                encrypted_text = encryption(matrix, pairs)
                with open(output_file, 'w') as file:
                    file.write(encrypted_text)
                print(f"File encrypted and saved to {output_file}")
            except FileNotFoundError:
                print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
            except Exception as e:
                print(f"An error occurred during encryption: {e}")

        elif choice == '2':
            input_file = input("Enter the path of the encrypted file (default: D:\\ET22BTCO039\\playfair\\encrypted.txt): ") or "D:\\ET22BTCO039\\playfair\\encrypted.txt"
            output_file = input("Enter the path where decrypted file should be stored (default: D:\\ET22BTCO039\\playfair\\decrypted.txt): ") or "D:\\ET22BTCO039\\playfair\\decrypted.txt"
            try:
                with open(input_file, 'r') as file:
                    encrypted_text = file.read().strip().replace('j', 'i')
                pairs = after_split(encrypted_text)
                decrypted_text = decryption(matrix, pairs)
                with open(output_file, 'w') as file:
                    file.write(decrypted_text)
                print(f"File decrypted and saved to {output_file}")
            except FileNotFoundError:
                print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
            except Exception as e:
                print(f"An error occurred during decryption: {e}")

        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
