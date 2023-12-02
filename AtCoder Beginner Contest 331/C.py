n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    sm = 0
    for j in range(n):
        if a[i] < a[j]:
            sm += a[j]
    b.append(sm)
print(*b)