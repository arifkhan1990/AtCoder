import math

def min_value_D(D):
    # Check if D is a perfect square
    sqrt_D = int(math.sqrt(D))
    if sqrt_D * sqrt_D == D:
        return 0

    # Initialize pointers
    left, right = 0, int(math.sqrt(D))

    # Initialize the minimum value
    min_val = float('inf')

    while left <= right:
        # Calculate the sum of squares
        current_sum = left**2 + right**2

        # Update the minimum value
        min_val = min(min_val, abs(current_sum - D))

        # Adjust pointers based on the comparison
        if current_sum < D:
            left += 1
        elif current_sum > D:
            right -= 1
        else:
            return 0

    return min_val

# Example usage:
D = int(input())
result = min_value_D(D)
print(result)
