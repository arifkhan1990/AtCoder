N, Q = map(int, input().split())
C = [(i + 1, 0) for i in range(N)]
C.reverse()

output = []

for _ in range(Q):
    query = input().split()
    query_type = int(query[0])
    
    if query_type == 1:
        s = query[1]
        x, y = C[-1]
        if s == "L":
            x -= 1
        elif s == "R":
            x += 1
        elif s == "U":
            y += 1
        elif s == "D":
            y -= 1
        C.append((x, y))
    else:
        x = int(query[1])
        output.append((C[-x][0], C[-x][1]))

# Print the output
for coordinates in output:
    print(f"{coordinates[0]} {coordinates[1]}")
