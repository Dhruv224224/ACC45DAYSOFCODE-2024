import math

# Hardcoded test cases
test_cases = [
    (100, 25, 40),
    (100, 29, 45),
    (46, 1, 2),
    (78, 15, 78)
]

# List to store results
results = []

# Process each test case
for H, X, Y in test_cases:
    # Calculate normal attacks only
    normal_attacks_only = math.ceil(H / X)
    
    # Calculate using the special attack
    remaining_health = H - Y
    if remaining_health <= 0:
        total_attacks_with_special = 1  # Special attack is enough to win
    else:
        normal_attacks_after_special = math.ceil(remaining_health / X)
        total_attacks_with_special = 1 + normal_attacks_after_special
    
    # Get the minimum attacks needed
    min_attacks = min(normal_attacks_only, total_attacks_with_special)
    results.append(min_attacks)

# Print results
for result in results:
    print(result)
