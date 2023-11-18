import hashlib
import os
import time

def targetGen(dif):
    if not 0 <= dif <= 256:
        raise ValueError("Input value 'dif' must be between 0 and 256 (inclusive).")

    # Create the binary string with dif number of 0's followed by (256 - dif) number of 1's
    binary_string = f"{'0' * dif}{'1' * (256 - dif)}"

    # Write the binary value to a file
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

            # Write the solution to a file
            with open('data/solution.txt', 'w') as file:
                file.write(str(s))

            return s, total_time

        s += 1

def verification(m, s, t):
    message = f"{m}{s}".encode('utf-8')
    hash_result = hashlib.sha256(message).hexdigest()

    if int(hash_result, 16) <= t:
        return 1
    else:
        return 0

def main():
    d = int(input("Enter the value of D: "))
    print("\nTarget:")
    print(targetGen(d))

    # Read message from file
    with open('data/input.txt', 'r') as file:
        message = file.read()

    # Read target from file
    with open('data/target.txt', 'r') as file:
        target_value = file.read()

    target = int(target_value, 2)  # Convert binary string to integer
    print(target)

    found_s, total_time = solutionGen(message, target)
    print(f"\nFound s: {found_s}")
    print(f"Total time: {total_time:.4f} seconds")

    # Verification
    result = verification(message, found_s, target)
    print(f"\nVerification Result: {result}")

if __name__ == "__main__":
    main()
