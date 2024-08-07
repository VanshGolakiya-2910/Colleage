import numpy as np
import os

def inp_key():
    inp_length = int(input("Enter the size of the matrix (n for an n x n matrix): "))
    key = input("Enter a key: ").replace(" ", "")
    
    if len(key) > inp_length**2:
        key = key[:inp_length**2]
    elif len(key) < inp_length**2:
        key = key.ljust(inp_length**2, 'X')  # Pad with 'X' if key is too short
    mat_key = create_key_matrix(key, inp_length)
    return mat_key

def create_key_matrix(key, size):
    key = key.lower()
    matrix = []
    index = 0
    for i in range(size):
        row = [ord(key[index + j]) - 97 for j in range(size)]
        matrix.append(row)
        index += size
    return np.array(matrix)

def create_text_matrix(text, size):
    text = text.lower()
    text_matrix = [ord(c) - 97 for c in text if c.isalpha()]  # Only letters
    if len(text_matrix) % size != 0:
        text_matrix.extend([0] * (size - len(text_matrix) % size))  # Pad text matrix
    return np.array(text_matrix).reshape(-1, size)

def mat_mul(mat1, mat2):
    try:
        return np.matmul(mat1, mat2) % 26
    except ValueError as e:
        return f"Matrix multiplication error: {e}"

def get_ans(matrix):
    return ''.join([chr(97 + int(num)) for num in matrix])

def inverse(matrix):
    try:
        det = int(round(np.linalg.det(matrix)))
        det_inv = pow(det, -1, 26)  # Modular inverse of the determinant
        adj_matrix = np.round(np.linalg.det(matrix) * np.linalg.inv(matrix)).astype(int) % 26
        inv_matrix = (det_inv * adj_matrix) % 26
        return inv_matrix
    except np.linalg.LinAlgError:
        return "Matrix inversion error"
    except Exception as e:
        return str(e)

def encrypt(plaintext, key_matrix):
    size = key_matrix.shape[0]
    text_matrix = create_text_matrix(plaintext, size)
    encrypted_matrix = mat_mul(text_matrix, key_matrix)
    encrypted_text = get_ans(encrypted_matrix.flatten())
    return encrypted_text

def decrypt(ciphertext, key_matrix):
    size = key_matrix.shape[0]
    # Compute the inverse of the key matrix
    inv_key_matrix = inverse(key_matrix)
    
    if isinstance(inv_key_matrix, str):
        return inv_key_matrix  # Return the error message if inversion failed

    text_matrix = create_text_matrix(ciphertext, size)
    decrypted_matrix = mat_mul(text_matrix, inv_key_matrix)
    decrypted_text = get_ans(decrypted_matrix.flatten())
    return decrypted_text.strip('X')  # Remove padding characters if any

def main_menu():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    # Generate key matrix once before menu
    key_matrix = inp_key()
    print("Key Matrix:")
    print(key_matrix)
    
    while True:
        choice = main_menu()

        if choice == '1':
            input_file = input("Enter the path of the input file (default: input.txt): ") or "input.txt"
            output_file = input("Enter the path where encrypted file should be stored (default: encrypted.txt): ") or "encrypted.txt"
            try:
                with open(input_file, 'r') as file:
                    plaintext = file.read().replace(" ", "")
                encrypted_text = encrypt(plaintext, key_matrix)
                with open(output_file, 'w') as file:
                    file.write(encrypted_text)
                print(f"File encrypted and saved to {output_file}")
                print(f"Encrypted Message: {encrypted_text}")
            except FileNotFoundError:
                print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
            except Exception as e:
                print(f"An error occurred during encryption: {e}")

        elif choice == '2':
            input_file = input("Enter the path of the encrypted file (default: encrypted.txt): ") or "encrypted.txt"
            output_file = input("Enter the path where decrypted file should be stored (default: decrypted.txt): ") or "decrypted.txt"
            try:
                with open(input_file, 'r') as file:
                    ciphertext = file.read().replace(" ", "")
                decrypted_text = decrypt(ciphertext, key_matrix)
                with open(output_file, 'w') as file:
                    file.write(decrypted_text)
                print(f"File decrypted and saved to {output_file}")
                print(f"Decrypted Message: {decrypted_text}")
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
