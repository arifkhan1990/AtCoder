# Read input values
N, S, K = map(int, input().split())

# Initialize total cost to 0
total_cost = 0

# Iterate through each type of product
for _ in range(N):
    P, Q = map(int, input().split())
    total_cost += P * Q  # Add the cost of each type of product to the total

# Calculate shipping fee
shipping_fee = 0 if total_cost >= S else K

# Calculate the total amount Takahashi will pay
total_amount = total_cost + shipping_fee

# Print the result
print(total_amount)
