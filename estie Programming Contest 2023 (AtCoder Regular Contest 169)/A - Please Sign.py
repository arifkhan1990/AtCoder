def perform_operations(a, p, n):
    dep = [0] * (n + 1)
    lim = [0] * (n + 1)

    for i in range(2, n + 1):
        dep[i] = dep[p[i-1]] + 1

    for i in range(1, n + 1):
        lim[dep[i]] += a[i]

    for i in range(n, -1, -1):
        if lim[i]:
            if lim[i] > 0:
                return "+"
            else:
                return "-"

    return "0"


n = int(input())
a = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
output = perform_operations(a, p, n)
print(output)