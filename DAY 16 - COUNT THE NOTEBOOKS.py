# Function to compute number of notebooks from given pulp in kilograms

def count_notebooks(N):
    return N * 10  # As N kg of pulp makes N * 10 notebooks


# Predefined test cases

T = 3  
test_cases = [1, 100, 50] 

# Loop through each test case and print the number of notebooks
\
for i in range(T):
    N = test_cases[i]                 # Get the value of N for this test case
    print(count_notebooks(N))         # Print the result for each test case
