# Predefined list of test cases for demonstration

test_cases = [(1, 5), (4, 2), (6, 6)]

# Process each test case

for X, Y in test_cases:
    if X < Y:
        print("BIKE")
    elif X > Y:
        print("CAR")
    else:
        print("SAME")
