# Function to count the number of Tuesdays in N days 

def count_tuesdays(n):

    return (n + 5) // 7  # Using integer division to calculate


# Define test cases

test_cases = [1, 10, 15, 16]  # Example test cases


# Store results for each test case

results = []

for n in test_cases:

    results.append(count_tuesdays(n))


# Print all results, each on a new line

for result in results:
    print(result)
