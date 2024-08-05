
def encryption(input_file, output_file, key):
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

def decryption(input_file, output_file, key):
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

# Example usage:
input_file = 'input.txt'
encrypted_file = 'encrypted.txt'
decrypted_file = 'decrypted.txt'
key = 1

# Encrypt input from input.txt and write to encrypted.txt
encryption(input_file, encrypted_file, key)

# Decrypt input from encrypted.txt and write to decrypted.txt
decryption(encrypted_file, decrypted_file, key)
