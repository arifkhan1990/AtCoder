def next_day(y, m, d, M, D):
    # Check if the given date is valid
    if 1000 <= y <= 9000 and 1 <= m <= M <= 99 and 1 <= d <= D <= 99:
        # Check if it's the last day of the month
        if d == D:
            # Check if it's the last month of the year
            if m == M:
                # If it's the last day of the last month, move to the next year
                return y + 1, 1, 1
            else:
                # If it's the last day of the month, move to the next month
                return y, m + 1, 1
        else:
            # If it's not the last day of the month, move to the next day
            return y, m, d + 1

# Read input from standard input
M, D = map(int, input().split())
y, m, d = map(int, input().split())

# Calculate the next day
result = next_day(y, m, d, M, D)
print(*result)
