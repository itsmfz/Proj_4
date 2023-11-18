def compute_target_binary(difficulty):
    """
    Compute the target value as a binary string based on the given difficulty.
    
    Parameters:
    - difficulty: Number of leading zeros required in the hash
    
    Returns:
    - target_binary: Binary string representing the target value for the Proof of Work
    """
    if not 0 <= difficulty <= 256:
        raise ValueError("Difficulty must be between 0 and 256 (inclusive).")

    # Compute the target binary string
    target_binary = '0' * difficulty + '1' * (256 - difficulty)
    return target_binary

# Example usage:
difficulty_level = 4  # Adjust difficulty level as needed
target_binary_value = compute_target_binary(difficulty_level)

print(f"Difficulty: {difficulty_level}")
print(f"Target Binary Value: {target_binary_value}")
