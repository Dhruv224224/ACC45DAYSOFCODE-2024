def is_possible(A, B, C, D):
    return C >= A and D >= B

# Number of test cases
T = 3  # Example: change this as needed

# Example test cases (you can modify these as needed)
test_cases = [
    (1, 5, 3, 5),
    (3, 4, 2, 6),
    (2, 2, 2, 2)
]

results = []
for i in range(T):
    A, B, C, D = test_cases[i]
    
    if is_possible(A, B, C, D):
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")

# Print all results for the test cases
for result in results:
    print(result)
