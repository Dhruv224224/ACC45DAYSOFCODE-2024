def captain_vice_captain_choices(test_cases):
    results = []
    for N in test_cases:
        choices = N * (N - 1)
        results.append(choices)
    return results

# Example usage
test_cases = [2, 3, ]  # replace with your list of N values
output = captain_vice_captain_choices(test_cases)
for result in output:
    print(result)
