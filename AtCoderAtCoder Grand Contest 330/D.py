def count_triples(N, grid):
    total_triples = 0

    for i in range(N):
        row_count_o = grid[i].count('o')
        for j in range(N):
            if grid[i][j] == 'o':
                col_count_o = sum(1 for k in range(N) if grid[k][j] == 'o')
                total_triples += (row_count_o - 1) * (col_count_o - 1)

    return total_triples



# Take user input for N and grid
N = int(input())
grid = [input().strip() for _ in range(N)]

# Calculate and print the result
result = count_triples(N, grid)
print(result)
