def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Sample input data
test_cases = [23, 13, 20, 1000, 99991]

# Results storage
results = []

for N in test_cases:
    if is_prime(N):
        results.append("yes")
    else:
        results.append("no")

# Print results
for result in results:
    print(result)
