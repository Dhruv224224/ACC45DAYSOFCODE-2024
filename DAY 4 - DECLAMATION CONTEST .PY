# Step 1: Get the input from the user

input_line = input("Enter four numbers (A B C X): ")     # Example input: "1 2 3 2"

# Step 2: Split the input and convert them to integers

A, B, C, X = map(int, input_line.split())

# Step 3: Check if X is one of A, B, or C

if X == A or X == B or X == C:

    print("Yes")               # Print Yes if there's a match
else:
    print("No")                # Print No if there's no match
