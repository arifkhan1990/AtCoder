def replace_center_with_t(matrix):
    N = len(matrix)
    center = (N - 1) // 2
    matrix[center][center] = 'T'

def generate_spiral_matrix(N):
    matrix = [[0] * N for _ in range(N)]

    left, right, top, bottom = 0, N - 1, 0, N - 1
    current_number = 1

    while left <= right and top <= bottom:
        # Move right
        for j in range(left, right + 1):
            matrix[top][j] = current_number
            current_number += 1
        top += 1

        # Move down
        for i in range(top, bottom + 1):
            matrix[i][right] = current_number
            current_number += 1
        right -= 1

        # Move left
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = current_number
            current_number += 1
        bottom -= 1

        # Move up
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = current_number
            current_number += 1
        left += 1

    replace_center_with_t(matrix)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Input
N = int(input())

# Generate and print spiral matrix
spiral_matrix = generate_spiral_matrix(N)
print_matrix(spiral_matrix)
