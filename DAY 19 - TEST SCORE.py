# Test cases hardcoded

test_cases = [
    (1, 8, 4),       # Test case 1
    (3, 6, 12),      # Test case 2
    (4, 5, 0),       # Test case 3
    (10, 10, 100),      # Test case 4
    (8, 5, 36)       # Test case 5
]

# Process each test case

for N, X, Y in test_cases:
    
    # Check the two conditions

    if Y % X == 0 and Y // X <= N:
        print("YES")
    else:
        print("NO")
