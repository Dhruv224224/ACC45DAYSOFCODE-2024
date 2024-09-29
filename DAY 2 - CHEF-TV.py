# Function to calculate the cost

def calculate_cost(N, X):
    # Calculate how many subscriptions we need

    subscriptions_needed = (N + 5) // 6
    # Calculate total cost

    total_cost = subscriptions_needed * X
    return total_cost

# Read number of test cases

T = int(input("Enter number of test cases: "))
for _ in range(T):
    # Read number of friends and cost of subscription

    N, X = map(int, input("Enter number of friends and subscription cost: ").split())
    # Calculate and print the total cost
    
    print(calculate_cost(N, X))
