def solve():
    # Example test cases
    test_cases = [
        (7, 5, 30),  # Test case 1
        (16, 5, 0),  # Test case 2
        (15, 9, 120),  # Test case 3
        (23, 1, 2130),  # Test case 4
    ]
    
    # Loop through each test case
    for X, Y, R in test_cases:
        # Calculate the number of extra sticks
        extra_sticks = R // 30
        
        # Calculate total sticks Chef ate
        total_sticks = X + extra_sticks
        
        # Calculate the number of plates needed to eat the total_sticks
        plates = (total_sticks + Y - 1) // Y
        
        # Output the result for this test case
        print(plates)

# Run the solve function
solve()
