import os
import secrets
from hashlib import sha256
from base64 import b64encode, b64decode
import glob
import hashlib
import time

def targetGen(dif):
    if not 0 <= dif <= 256:
        raise ValueError("Input value 'dif' must be between 0 and 256 (inclusive).")

    # Create the binary string with dif number of 0's followed by (256 - dif) number of 1's
    binary_string = f"{'0' * dif}{'1' * (256 - dif)}"

    # Write the binary string to a text file
    with open('data/target.txt', 'w') as file:
        file.write(binary_string)

    return binary_string

def solutionGen(m, target_value):
    start_time = time.time()

    # Convert the binary string to an integer
    t = int(target_value, 2)
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

def verifySolution(m, s, t):
    message = f"{m}{s}".encode('utf-8')
    hash_result = hashlib.sha256(message).hexdigest()

    if int(hash_result, 16) <= t:
        return 1  # Valid solution
    else:
        return 0  # Invalid solution

def main():
    # Read the difficulty value from user input
    d = int(input("Enter the value of D "))

    # Generate and print the target
    print("\nTarget:")
    target_value = targetGen(d)
    print(target_value)

    # Read the input message from file
    file_path = "data/input.txt"
    with open(file_path, 'r') as file:
        message = file.read()

    # Read the target from file
    file_path = "data/target.txt"
    with open(file_path, 'r') as file:
        target_value = file.read()

    # Generate, print, and write the solution to file
    found_s, total_time = solutionGen(message, target_value)
    print(f"Found s: {found_s}")

    # Write the solution to file
    with open("data/solution.txt", 'w') as file:
        file.write(str(found_s))  # Convert found_s to string before writing

    print(f"Total time: {total_time:.4f} seconds")

    # Verification
    verification_result = verifySolution(message, found_s, int(target_value, 2))
    print(f"Verification result: {verification_result}")

if __name__ == "__main__":
    main()
