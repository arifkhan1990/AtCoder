def count_triples(N, grid):
    total_triples = 0

    row_count_o = [0] * N
    col_count_o = [0] * N

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                row_count_o[i] += 1
                col_count_o[j] += 1

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                total_triples += (row_count_o[i] - 1) * (col_count_o[j] - 1)

    return total_triples

# Take user input for N and grid
N = int(input())
grid = [input().strip() for _ in range(N)]

# Calculate and print the result
result = count_triples(N, grid)
print(result)
