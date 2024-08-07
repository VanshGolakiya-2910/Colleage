import numpy as np
import random
import math

def is_valid_key(matrix):
    det = int(np.round(np.linalg.det(matrix))) % 26
    return math.gcd(det, 26) == 1

def generate_valid_key(size):
    while True:
        key = np.random.randint(0, 26, (size, size))
        if is_valid_key(key):
            return key

def convert_to_string(matrix):
    return ''.join([chr(65 + num) for row in matrix for num in row])

def generate_keys():
    keys = {
        "3x3": [],
        "4x4": []
    }
    
    # Generate 4 keys for 3x3
    for _ in range(4):
        key = generate_valid_key(3)
        keys["3x3"].append(convert_to_string(key))
    
    # Generate 4 keys for 4x4
    for _ in range(4):
        key = generate_valid_key(4)
        keys["4x4"].append(convert_to_string(key))
    
    return keys

# Generate and print keys
keys = generate_keys()
for size, key_list in keys.items():
    print(f"Valid keys for {size} matrices:")
    for key in key_list:
        print(key)
    print()
