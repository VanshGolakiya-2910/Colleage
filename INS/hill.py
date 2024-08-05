import numpy as np

def inp_key():
    while True:
        inp_length = int(input("Enter the size of the matrix (n for an n x n matrix): "))
        key = input("Enter a key: ").replace(" ", "")
        
        if len(key) > inp_length**2:
            key = key[:inp_length**2]
        elif len(key) < inp_length**2:
            key = key.ljust(inp_length**2, 'x')  # Pad with 'x' if key is too short
        
        mat_key = create_key_matrix(key, inp_length)
        
        if is_invertible(mat_key, 26):
            return mat_key
        else:
            print("The key matrix is not invertible. Please enter a different key.")

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
    text_matrix = [ord(c) - 97 for c in text]
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

def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus

def is_invertible(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    try:
        pow(det, -1, modulus)
        return True
    except ValueError:
        return False

def encrypt(plaintext, key_matrix):
    size = key_matrix.shape[0]
    text_matrix = create_text_matrix(plaintext, size)
    encrypted_matrix = mat_mul(text_matrix, key_matrix)
    encrypted_text = get_ans(encrypted_matrix.flatten())
    return encrypted_text

def decrypt(ciphertext, key_matrix):
    size = key_matrix.shape[0]
    inv_key_matrix = mod_inverse(key_matrix, 26)
    
    if isinstance(inv_key_matrix, str):
        return inv_key_matrix  # Return the error message if inversion failed

    text_matrix = create_text_matrix(ciphertext, size)
    decrypted_matrix = mat_mul(text_matrix, inv_key_matrix)
    decrypted_text = get_ans(decrypted_matrix.flatten())
    return decrypted_text.strip('x')  # Remove padding characters if any

def main_menu():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    key_matrix = inp_key()
    print("Key Matrix:")
    print(key_matrix)
   
    while True:
        choice = main_menu()
       
        if choice == '1':
            input_file = "INS\input.txt"
            output_file = "INS\encrypted.txt"
            try:
                with open(input_file, 'r') as file:
                    plaintext = file.read().strip().replace(" ", "")
                encrypted_text = encrypt(plaintext, key_matrix)
                with open(output_file, 'w') as file:
                    file.write(encrypted_text)
                print(f"File encrypted and saved to {output_file}")
                print("Encrypted text:", encrypted_text)
            except FileNotFoundError:
                print(f"The file '{input_file}' does not exist. Please check the file path and try again.")
            except Exception as e:
                print(f"An error occurred during encryption: {e}")

        elif choice == '2':
            input_file = "INS\encrypted.txt"
            output_file = "INS\decrypted.txt"
            try:
                with open(input_file, 'r') as file:
                    ciphertext = file.read().strip().replace(" ", "")
                decrypted_text = decrypt(ciphertext, key_matrix)
                with open(output_file, 'w') as file:
                    file.write(decrypted_text)
                print(f"File decrypted and saved to {output_file}")
                print("Decrypted text:", decrypted_text)
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
