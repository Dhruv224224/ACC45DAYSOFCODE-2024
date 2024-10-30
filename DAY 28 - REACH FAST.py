def min_steps_to_reach(test_cases):
    results = []
    for A, B, K in test_cases:
        distance = abs(B - A)
        steps = (distance + K - 1) // K  # Ceiling division to get the number of steps
        results.append(steps)
    return results

# Example usage:
test_cases = [
    (10, 20, 3),
    (36, 36, 5),
    (50, 4, 100),
    (30, 4, 2)
]

results = min_steps_to_reach(test_cases)

for result in results:
    print(result)
