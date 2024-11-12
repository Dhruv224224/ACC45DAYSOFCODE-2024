def max_people_for_bath(T, test_cases):
    results = []
    for case in test_cases:
        X, Y = case
        # Calculate the amount of water required for one person
        water_per_person = 2 * Y
        # Calculate the maximum number of people that can take a bath
        max_people = X // water_per_person
        results.append(max_people)
    return results

# Example test cases
T = 4  # Number of test cases
test_cases = [
    (10, 6),  # Test case 1
    (25, 1),  # Test case 2
    (100, 10), # Test case 3
    (30, 40)  # Test case 4
]

# Solve the problem and output the results
results = max_people_for_bath(T, test_cases)

# Printing results
for result in results:
    print(result)
