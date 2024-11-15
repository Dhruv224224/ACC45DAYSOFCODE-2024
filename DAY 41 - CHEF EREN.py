def calculate_total_duration(N, A, B):
    # Calculate number of odd-indexed episodes
    odd_count = (N + 1) // 2  # Odd indexed episodes: 1, 3, 5, ..., up to N
    # Calculate number of even-indexed episodes
    even_count = N // 2       # Even indexed episodes: 2, 4, 6, ..., up to N
    
    # Total duration is odd_count * B + even_count * A
    total_duration = odd_count * B + even_count * A
    return total_duration

# Example input values
T = 3  # Number of test cases
test_cases = [
    (1, 2, 2),  # (N, A, B) for first test case
    (2, 3, 4),  # (N, A, B) for second test case
    (4, 20, 30) # (N, A, B) for third test case
]

# Process each test case and print the result
for case in test_cases:
    N, A, B = case
    print(calculate_total_duration(N, A, B))
