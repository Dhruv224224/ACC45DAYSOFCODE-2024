# Hardcoded test cases (Example input)

T = 4        # Number of test cases
test_cases = [
    (1, 1, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 1),
    (1, 1, 1, 1)
]

# Process each test case

for i in range(T):
    R1, R2, R3, R4 = test_cases[i]
    
    # Check if all referees say the ball is inside limits (i.e., all 0)
    
    if R1 == 0 and R2 == 0 and R3 == 0 and R4 == 0:
        print("IN")
    else:
        print("OUT")
