import math

def solve():
    # Number of test cases
    T = 4  # Example: 4 test cases
    
    # List of test cases as tuples (N, A, B)
    test_cases = [
        (4, 10, 5),     # Test case 1: N=4, A=10, B=5
        (16, 30, 5),    # Test case 2: N=16, A=30, B=5
        (32, 45, 15),   # Test case 3: N=32, A=45, B=15
        (1024, 23, 9)   # Test case 4: N=1024, A=23, B=9
    ]
    
    # Process each test case
    for i in range(T):
        N, A, B = test_cases[i]  # Get N, A, B for the current test case
        
        # Calculate the number of rounds (log2(N) since N is a power of 2)
        rounds = int(math.log2(N))
        
        # Calculate the total time: time for rounds + time for breaks
        total_time = rounds * A + (rounds - 1) * B
        
        # Output the total time
        print(total_time)

# Call the solve function to execute
solve()
