def solve():
    # Number of test cases
    T = 4

    # Predefined test cases (P, Q, R, S)
    test_cases = [
        (1, 1, 1, 10),  # First test case
        (30, 20, 6, 4),  # Second test case
        (100, 90, 3, 4),   # Third test case
        (14 , 15 ,16 , 17),  # fourth test case
    ]

    # Loop through each test case and check for monopoly
    for P, Q, R, S in test_cases:
        # Check if any company has a monopoly
        if P > Q + R + S or Q > P + R + S or R > P + Q + S or S > P + Q + R:
            print("YES")
        else:
            print("NO")
solve()


  
