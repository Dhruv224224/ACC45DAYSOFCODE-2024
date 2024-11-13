# Number of test cases
T = 3

# List of test case prices
test_cases = [
    (6, 2, 4),
    (3, 3, 3),
    (8, 4, 4)
]

# Iterate over each test case
for i in range(T):
    # Prices of the three items
    A, B, C = test_cases[i]
    
    # Calculate the total amount Chef needs to pay (sum of the two highest prices)
    total_to_pay = A + B + C - min(A, B, C)
    
    # Output the result for the current test case
    print(total_to_pay)
