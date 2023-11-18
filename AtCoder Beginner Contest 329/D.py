from collections import Counter
br = [0]*200005
ans = 1

n , m = map(int, input().split())
ar = list(map(int,input().split()))

for i in range(m):
    x = ar[i]
    br[x] += 1
    
    if br[x] > br[ans] or (br[x] == br[ans] and x < ans):
        ans = x
    
    print(ans)
