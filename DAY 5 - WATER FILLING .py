# Step 1: Read the number of test cases
T = int(input("Enter number of test cases: "))

# Step 2: Loop through each test case
for i in range(T):
    # Read the status of the three bottles
    B1, B2, B3 = input("Enter the status of bottles (0 or 1): ").split()
    
    # Convert the input from strings to integers
    B1 = int(B1)
    B2 = int(B2)
    B3 = int(B3)
    
    # Step 3: Count how many bottles are empty
    empty_count = 0  # Start with zero empty bottles
    if B1 == 0:
        empty_count = empty_count + 1  # Count B1 if empty
    if B2 == 0:
        empty_count = empty_count + 1  # Count B2 if empty
    if B3 == 0:
        empty_count = empty_count + 1  # Count B3 if empty
    
    # Step 4: Check if at least two bottles are empty
    if empty_count >= 2:
        print("Water filling time")  # Fill the bottles
    else:
        print("Not now")  # Do not fill the bottles
