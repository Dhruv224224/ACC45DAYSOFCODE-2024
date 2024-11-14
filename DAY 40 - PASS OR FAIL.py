# Predefined test cases
test_cases = [
    (5, 2, 3),
    (5, 2, 4),
    (4, 0, 0)
]

# Process each test case
for N, X, P in test_cases:
    # Calculate the total score
    score = 4 * X - N
    
    # Check if Chef passes or fails
    if score >= P:
        print("PASS")
    else:
        print("FAIL")
