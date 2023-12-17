s = input()
t = input()

d1 = abs(ord(s[0]) - ord(s[1]))
d2 = abs(ord(t[0]) - ord(t[1]))

d1 = min(d1, 5 - d1)
d2 = min(d2, 5 - d2)

print("Yes" if d1 == d2 else "No")