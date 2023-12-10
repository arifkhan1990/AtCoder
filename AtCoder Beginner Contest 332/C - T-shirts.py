def min_tshirts_to_buy(N, M, S):
    t = 0  # Total T-shirts needed
    plain_tshirts = M
    ps = 0
    ts = 0
    ans = 0
    for i in range(N):

        if S[i] == '1':
             ps += 1
        elif S[i] == '2':
             ts += 1
        else:
             t =  (ps - plain_tshirts if ps > plain_tshirts else 0)
             ans = max(ans, t+ts)
             t = 0
             ps = 0
             ts = 0
    ans = max(ans, max(ans, ts+(ps - plain_tshirts if ps > plain_tshirts else 0)))
    return ans

# Example usage:
N, M = map(int, input().split())
S = input().strip()
result = min_tshirts_to_buy(N, M, S)
print(result)
