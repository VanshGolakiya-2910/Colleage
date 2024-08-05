import numpy as np

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

def inverse(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix) % 26
        # Convert to integer matrix
        inv_matrix = np.round(inv_matrix).astype(int)
        # Modulo inverse correction
        inv_matrix = inv_matrix % 26
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

# Final execution block
if __name__ == "__main__":
    # Input key and create key matrix
    key_matrix = inp_key()
    print("Key Matrix:")
    print(key_matrix)

    # Encrypting a message
    plaintext = input("Enter plaintext to encrypt: ").replace(" ", "")
    encrypted_text = encrypt(plaintext, key_matrix)
    print("Encrypted Text:")
    print(encrypted_text)

    # Decrypting the message
    ciphertext = input("Enter ciphertext to decrypt: ").replace(" ", "")
    decrypted_text = decrypt(ciphertext, key_matrix)
    print("Decrypted Text:")
    print(decrypted_text)
