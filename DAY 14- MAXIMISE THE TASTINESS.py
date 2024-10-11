# Sample input data as variables
T = 2  # Number of test cases

# Test cases, where each is a tuple (a, b, c, d)
test_cases = [
    (3, 5, 6, 2),
    (16, 15, 5, 4),
]

# Loop over each test case
for i in range(T):
    # Unpack the test case
    a, b, c, d = test_cases[i]
    
    # Compute the maximum tastiness
    max_tastiness = max(a + c, a + d, b + c, b + d)
    
    # Print the result
    print(max_tastiness)
