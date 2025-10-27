def max_path_in_pyramid(pyramid):
    for row in range(1,len(pyramid)):
        for col in range (1, len(pyramid[row])):
            if col == 0:
                pyramid[row][col] = pyramid[row][col] + pyramid[row - 1][col]
            elif col == len(pyramid[row]) - 1:
                pyramid[row][col] = pyramid[row][col] + pyramid[row - 1][col-1]
            else:
                pyramid[row][col] = pyramid[row][col] + max(pyramid[row - 1][col-1], pyramid[row - 1][col])
    return max(pyramid[-1])
print(max_path_in_pyramid([[1], [3, 2], [4, 5, 6]]))