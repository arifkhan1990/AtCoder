def water_operations(K, G, M):
    glass_water = 0
    mug_water = 0

    for _ in range(K):
        if glass_water == G:
            glass_water = 0
        elif mug_water == 0:
            mug_water = M
        else:
            transfer_amount = min(mug_water, G - glass_water)
            glass_water += transfer_amount
            mug_water -= transfer_amount

    return glass_water, mug_water


K, G, M = map(int, input().split())
result = water_operations(K, G, M)

# Printing the result
print(result[0], result[1])
