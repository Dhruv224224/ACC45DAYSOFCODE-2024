# Function to calculate the minimum number of bags required

def min_bags(N, K, M):

    # The total capacity of one bag is K * M

    capacity_per_bag = K * M

    # Calculate the minimum number of bags required using ceiling division

    return (N + capacity_per_bag - 1) // capacity_per_bag

# Test Cases (you can add more test cases by adding to the list)

test_cases = [
    (6, 2, 3), 
    (3, 1, 2),
    (8 , 4 ,1 ),
    (25 , 4 , 2),  
]

# Process each test case

for N, K, M in test_cases:
    
    # Print the result for this test case

    print(min_bags(N, K, M))
