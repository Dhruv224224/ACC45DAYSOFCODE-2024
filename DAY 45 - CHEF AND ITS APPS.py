def solve():
    # Test cases hardcoded
    test_cases = [
        (10, 1, 2, 3),
        (9, 4, 5, 1),
        (15, 5, 10, 15),
        (100, 20, 30, 75)
    ]
    
    # Iterate through the test cases
    for S, X, Y, Z in test_cases:
        # Calculate free space available
        free_space = S - (X + Y)
        
        # Case 1: Check if free space is enough to install the new app
        if free_space >= Z:
            print(0)  # No apps need to be deleted
        # Case 2: Check if deleting one app is enough
        elif S - X >= Z or S - Y >= Z:
            print(1)  # One app needs to be deleted
        # Case 3: If deleting both apps is necessary
        else:
            print(2)  # Both apps need to be deleted

# Call the solve function
solve()
