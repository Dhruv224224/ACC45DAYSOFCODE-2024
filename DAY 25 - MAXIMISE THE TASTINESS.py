def max_tastiness(test_cases):
    results = []
    for a, b, c, d in test_cases:
        # Calculate all possible tastiness values
        tastiness1 = a + c
        tastiness2 = a + d
        tastiness3 = b + c
        tastiness4 = b + d
        
        # Find the maximum tastiness
        max_tastiness = max(tastiness1, tastiness2, tastiness3, tastiness4)
        results.append(max_tastiness)
    
    return results

# Example test cases
test_cases = [
    (3, 5, 6, 2),  # Example from sample 1
    (16, 15, 5, 4) # Example from sample 2
]

# Calculate results
results = max_tastiness(test_cases)

# Output results
for result in results:
    print(result)
