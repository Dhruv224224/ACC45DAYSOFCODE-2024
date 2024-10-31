def find_server(P, Q):
    total_serves = P + Q
    serve_in_block = total_serves % 4
    
    if serve_in_block == 0 or serve_in_block == 1:
        return "Alice"
    else:
        return "Bob"

# List of test cases (P, Q)
test_cases = [
    (0, 0),
    (0, 2),
    (2, 2),
    (4, 7)
]

# Process each test case
for P, Q in test_cases:
    print(find_server(P, Q))
