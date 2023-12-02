def min_money_required(N, S, M, L):
    # Initialize the minimum cost to a large value
    min_cost = float('inf')

    # Iterate through all possible quantities of each pack
    for s_quantity in range(N + 1):
        for m_quantity in range(N + 1):
            for l_quantity in range(N + 1):
                # Calculate the total number of eggs for the current combination
                total_eggs = s_quantity * 6 + m_quantity * 8 + l_quantity * 12

                # Check if the total number of eggs is greater than or equal to N
                if total_eggs >= N:
                    # Calculate the cost for the current combination
                    cost = s_quantity * S + m_quantity * M + l_quantity * L

                    # Update the minimum cost if the current cost is smaller
                    min_cost = min(min_cost, cost)

    return min_cost

# Input values
N, S, M, L = map(int, input().split())

# Calculate and print the minimum amount of money required
result = min_money_required(N, S, M, L)
print(result)
