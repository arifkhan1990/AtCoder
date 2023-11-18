n = int(input())
s = input()
ans = [0]*26
a = 0
i = 0
while i < n:
    res = 1
    while i+1 < n and s[i] == s[i+1]:
        res += 1
        i += 1

    ans[ord(s[i])-ord('a')] = max(ans[ord(s[i])-ord('a')], res)
    i += 1

for i in range(26):
    a += ans[i]

print(a)
