import os            # Operating system-related functions
import secrets       # Cryptographically strong random number generation
from hashlib import sha256  # Hash function for secure hashing
from base64 import b64encode, b64decode  # Encoding/decoding data in base64 format
import glob # Import the glob module for file path pattern matching

def targetGen(dif):
    if not 0 <= dif <= 256:
        raise ValueError("Input value 'dif' must be between 0 and 256 (inclusive).")

    # Create the binary string with dif number of 0's followed by (256 - dif) number of 1's
    binary_string = f"{'0' * dif}{'1' * (256 - dif)}"

    # Write the binary and decimal values to a text file
    with open('data/target.txt', 'w') as file:
        file.write(binary_string)


    return binary_string

def main():
    d = int(input("Enter the value of D "))
    print(targetGen(d))

if __name__ == "__main__":
    main()