# test cases 
T = 4
test_cases = [(5, 0), (4, 2), (3, 3) , (10 , 2)]

for i in range(T):
    N, X = test_cases[i]

    print(min(X, N - X))
