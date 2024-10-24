def find_degree_of_polynomial(test_cases):
    results = []
    for case in test_cases:
        N, coefficients = case
        degree = 0
        for i in range(N):
            if coefficients[i] != 0:
                degree = i  # Update degree to current index
        results.append(degree)
    return results

# Example input directly defined in the code
test_cases = [
    (1, [5]),          # Test case 1
    (2, [-3, 3]),     # Test case 2
    (3, [0, 0, 5]),   # Test case 3
    (4, [1, 2, 4, 0]) # Test case 4
]

# Get results
degrees = find_degree_of_polynomial(test_cases)

# Print results
for degree in degrees:
    print(degree)
