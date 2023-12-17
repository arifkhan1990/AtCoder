M = 15
a = [0 for i in range(M)]
a[0] = 1
for i in range(1, M):
    a[i] = 10 * a[i - 1] + 1
s = set()
for i in range(M):
    for j in range(M):
        for k in range(M):
            s.add(a[i] + a[j] + a[k])
print(sorted(list(s))[int(input()) - 1])