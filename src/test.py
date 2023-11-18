import os            # Operating system-related functions
import secrets       # Cryptographically strong random number generation
from hashlib import sha256  # Hash function for secure hashing
from base64 import b64encode, b64decode  # Encoding/decoding data in base64 format
import glob # Import the glob module for file path pattern matching
import hashlib
import time

def targetGen(dif):
    if not 0 <= dif <= 256:
        raise ValueError("Input value 'dif' must be between 0 and 256 (inclusive).")

    # Create the binary string with dif number of 0's followed by (256 - dif) number of 1's
    binary_string = f"{'0' * dif}{'1' * (256 - dif)}"

    # Write the binary and decimal values to a text file
    with open('data/target.txt', 'w') as file:
        file.write(binary_string)


    return binary_string

def solutionGen(m, t):
    
    start_time = time.time()
    
    s = 0
    while True:
        message = f"{m}{s}".encode('utf-8')
        hash_result = hashlib.sha256(message).hexdigest()

        print(f"Trying s = {s}, Hash: {hash_result}")

        if int(hash_result, 16) <= t:
            end_time = time.time()
            total_time = end_time - start_time
            return s, total_time

        s += 1

def main():
    d = int(input("Enter the value of D "))
    print("\nTarget:")
    print(targetGen(d))


    file_path = "data/input.txt"  # Replace with the actual file path
    with open(file_path, 'r') as file:
        # Read the contents of the file into a variable
        message = file.read()

    file_path = "data/target.txt"  # Replace with the actual file path
    with open(file_path, 'r') as file:
        # Read the contents of the file into a variable
        target_value = file.read()

    target = int(target_value)
    print(target)
    found_s, total_time = solutionGen(message, target)
    print(f"Found s: {found_s}")
    print(f"Total time: {total_time:.4f} seconds")

if __name__ == "__main__":
    main()