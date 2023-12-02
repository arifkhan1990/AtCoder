def count_black_squares(N, P, queries):
    # Calculate cumulative sum for each row
    row_sum = [[0] * (N + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            row_sum[i][j + 1] = row_sum[i][j] + (P[i][j % N] == 'B')

    # Calculate cumulative sum for each column
    col_sum = [[0] * (N + 1) for _ in range(N)]
    for j in range(N):
        for i in range(N):
            col_sum[j][i + 1] = col_sum[j][i] + (P[i % N][j] == 'B')

    A, B, C, D = queries
    black_count = 0

    # Calculate black squares within the specified rectangular area
    black_count += row_sum[A % N][min(N, D + 1)] - row_sum[A % N][B % N]
    black_count += col_sum[B % N][min(N, C + 1)] - col_sum[B % N][A % N]


    return black_count

# Taking user input
N, Q = map(int, input().split())
P = [input().split() for _ in range(N)]
for _ in range(Q):
    queries = map(int, input().split())

    result = count_black_squares(N, P, queries)
    print(result)
