# Function to solve the problem
def cooler_dilemma(T, test_cases):
    results = []
    
    for X, Y in test_cases:
        if X >= Y:
            results.append(0)          # Chef should not rent the cooler
        else:
            results.append(Y // X)     # Maximum months for which renting is cheaper
    
    return results

# Sample input
T = 2     # Number of test cases
test_cases = [
    (5, 12),     # Test case 1
    (5, 5),      # Test case 2
    
]

# Solve the problem and get the results
results = cooler_dilemma(T, test_cases)

# Output the results
for result in results:
    print(result)
