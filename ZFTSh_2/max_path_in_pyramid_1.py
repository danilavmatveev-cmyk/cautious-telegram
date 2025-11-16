def max_path_in_pyramid(pyramid):

    dp = pyramid[-1].copy()


    for row in range(len(pyramid) - 2, -1, -1):
        current_dp = []
        for col in range(len(pyramid[row])):

            max_below = max(dp[col], dp[col + 1])
            current_dp.append(pyramid[row][col] + max_below)
        dp = current_dp

    return dp[0]
print(max_path_in_pyramid([[10], [20, 30], [40, 50, 60], [70, 80, 90, 100]]))