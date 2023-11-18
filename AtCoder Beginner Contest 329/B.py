n = int(input())
ar = list(set(map(int,input().split())))
ar.sort()
print(ar[-2])