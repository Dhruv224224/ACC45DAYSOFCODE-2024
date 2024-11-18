def is_valid_game(n, x):
    return x % n == 0

# Test cases
test_cases = [
    (3, 3),  # First test case: N=3, X=3
    (4, 2),  # Second test case: N=4, X=2
    (2, 4)   # Third test case: N=2, X=4
]

# Process each test case
for N, X in test_cases:
    if is_valid_game(N, X):
        print("YES")
    else:
        print("NO")
