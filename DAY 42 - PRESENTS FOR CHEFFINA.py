def solve():
    # Hardcoded test cases
    test_cases = [5, 4]  # Example test cases

    for N in test_cases:
        # Calculate the total coins required
        coins = 4 * (N // 5) + (N % 5)
        print(coins)

# Driver code to invoke the function
solve()
