def generate_triples(N):
    triples = []
    for x in range(N + 1):
        for y in range(N + 1):
            z1 = N - (x + y)
            for z in range(z1+1):
                if 0 <= z <= N:
                    triples.append([x, y, z])
    # triples.sort()
    return triples

N = int(input())
ans = generate_triples(N)
for x in ans:
    print(*x)