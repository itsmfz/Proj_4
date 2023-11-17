import hashlib
import random
import string

def compute_target(difficulty):
    # Compute the target based on the difficulty
    target = int('0' * difficulty + '1' * (256 - difficulty), 2)
    return target

def write_target_to_file(target, filename):
    # Write the target to a file
    with open(filename, 'w') as file:
        file.write(str(target))

def compute_pow_solution(message, target):
    # Find a valid POW solution
    while True:
        solution = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
        data = message + solution
        hash_value = int(hashlib.sha256(data.encode()).hexdigest(), 16)
        if hash_value <= target:
            return solution

def write_solution_to_file(solution, filename):
    # Write the solution to a file
    with open(filename, 'w') as file:
        file.write(solution)

def verify_pow_solution(message, solution, target):
    # Verify if the POW solution is valid
    data = message + solution
    hash_value = int(hashlib.sha256(data.encode()).hexdigest(), 16)
    return hash_value <= target

# Example usage:
difficulty = 5
message = "Hello, world!"

target = compute_target(difficulty)
write_target_to_file(target, 'target.txt')

solution = compute_pow_solution(message, target)
write_solution_to_file(solution, 'solution.txt')

is_valid_solution = verify_pow_solution(message, solution, target)
print("Is the solution valid?", is_valid_solution)
