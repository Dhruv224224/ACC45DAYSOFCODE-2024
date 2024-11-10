# Predefined test cases (angles of quadrilaterals)
test_cases = [
    [10, 20, 30, 300],   # First test case
    [10, 20, 170, 160],  # Second test case
    [179, 1, 179, 1]     # Third test case
]

# Loop over each test case
for angles in test_cases:
    # Check if the quadrilateral is cyclic by checking the sum of opposite angles
    if angles[0] + angles[2] == 180 and angles[1] + angles[3] == 180:
        print("YES")
    else:
        print("NO")
