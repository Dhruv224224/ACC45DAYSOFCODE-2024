def solve():
    # Test cases and numbers
    T = 3  # Number of test cases
    test_cases = [(1, 10), (1, 5), (4, 9)]  # List of test cases (pairs of A, B)

    for i in range(T):
        A, B = test_cases[i]  # Get A and B for each test case
        C = 21 - (A + B)  # Calculate the third number C
        if 1 <= C <= 10:  # Check if C is between 1 and 10
            print(C)
        else:
            print(-1)

# Call the solve function to execute
solve()
