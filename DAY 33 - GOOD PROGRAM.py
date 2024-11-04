# Predefined list of test cases
test_cases = [8, 17, 52, 3]

# Iterate through each test case
for N in test_cases:
    # Check if N is divisible by 4
    if N % 4 == 0:
        print("Good")
    else:
        print("Not Good")
