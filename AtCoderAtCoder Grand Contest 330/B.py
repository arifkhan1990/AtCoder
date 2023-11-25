def find_X_values(A, L, R):
    result = []
    for ai in A:
        if ai < L:
            result.append(L)
        elif ai > R:
            result.append(R)
        else:
            result.append(ai)
    return result

# Take user input
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# Call the function
X_values = find_X_values(A, L, R)

# Print the result
print(*X_values)
