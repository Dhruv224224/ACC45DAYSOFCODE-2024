# Function to calculate the minimum time to catch the thief
def police_and_thief(t, cases):
    results = []
    for i in range(t):
        X, Y = cases[i]
        # The time is simply the absolute difference between X and Y
        results.append(abs(X - Y))
    return results

# Example of how to call the function with test cases
T = 3  # Number of test cases
cases = [(1, 3), (2, 1), (1, 1)]  # List of tuples, each representing (X, Y)

# Get the results
results = police_and_thief(T, cases)

# Output the results
for result in results:
    print(result)
