# Example input (hardcoded)
T = 4 # Number of test cases
test_cases = [
    (5, 2, 1, 6),  # W = 10, X = 5, Y = 5, Z = 5
    (7, 9, 7, 2),   # W = 8, X = 5, Y = 5, Z = 5
    (20, 8, 10, 12),  # W = 12, X = 6, Y = 6, Z = 6
    (20, 10, 11, 12),
]

# Process each test case
for i in range(T):
    W, X, Y, Z = test_cases[i]
    
    # Check all combinations of X, Y, Z to see if they can sum up to W
    if (W == X or W == Y or W == Z or 
        W == X + Y or W == X + Z or W == Y + Z or
        W == X + Y + Z):
        print("YES")
    else:
        print("NO")
