# Hardcoded test cases
test_cases = [
    (3, ["START38", "LTIME108", "START38"]),
    (4, ["LTIME108", "LTIME108", "LTIME108", "START38"]),
    (2, ["LTIME108", "LTIME108"]),
    (6, ["START38", "LTIME108", "LTIME108", "LTIME108", "START38", "LTIME108"])
]

# Process each test case
for N, contest_codes in test_cases:
    # Initialize counters
    count_start38 = 0
    count_ltime108 = 0
    
    # Count each contest code
    for code in contest_codes:
        if code == 'START38':
            count_start38 += 1
        elif code == 'LTIME108':
            count_ltime108 += 1
    
    # Print the results
    print(count_start38, count_ltime108)
