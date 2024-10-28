def count_wolverine_minions(test_cases):
    results = []
    for case in test_cases:
        N, K = case[0]
        characteristic_values = case[1]
        count = 0
        
        for value in characteristic_values:
            new_value = value + K
            if new_value % 7 == 0:
                count += 1
        
        results.append(count)
    
    return results

# Example usage:
# Define the number of test cases and their data
T = 1
test_cases = [
    ((5, 10), [2, 4, 1, 35, 1]),  # First test case
]

# Get the results
results = count_wolverine_minions(test_cases)

# Print the output
for result in results:
    print(result)
