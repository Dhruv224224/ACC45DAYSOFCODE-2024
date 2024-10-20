import math

# Function to calculate total time for the event

def total_time_for_event(N, A, B):
    rounds = int(math.log2(N))          # Calculate number of rounds
    total_time_rounds = rounds * A          # Total time spent in rounds
    total_time_breaks = (rounds - 1) * B          # Total time spent in breaks
    return total_time_rounds + total_time_breaks          # Total time for the event

# Example test cases

test_cases = [
    (4, 10, 5),           # Test case 1
    (16, 30, 5),          # Test case 2
    (32, 45, 15),         # Test case 3
    (1024, 23, 9)         # Test case 4
]

# Processing each test case and printing the result

for N, A, B in test_cases:
    result = total_time_for_event(N, A, B)
    print(result)
        