# Predefined input data (for example purposes)
test_cases = [
    (5, 3),
    (4, 1),
    (1, 1),
    (2 , 1),
]

# Process each test case

for X, Y in test_cases:

    # Check if Y is at least 50% of X

    if 2 * Y >= X:
        print("YES")
    else:
        print("NO")
