# Step 1: Read number of test cases

T = int(input("Enter number of test cases: "))    

# Step 2: For each test case

for _ in range(T):

    # Step 3: Read X and Y

    X, Y = map(int, input("Enter X and Y: ").split())    
    
    # Step 4: Calculate total hours

    total_hours = (4 * X) + Y
    
    # Step 5: Print the result

    print(total_hours)     # Outputs the total hours
