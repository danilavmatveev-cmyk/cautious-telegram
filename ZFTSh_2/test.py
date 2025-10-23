def grasshopper_with_obstacles(n, obstacles):
    if n < 0:
        return 0


    blocked_points = set(obstacles)

    dp = [0] * (n + 1)


    if 0 in blocked_points:
        return 0
    else:
        dp[0] = 1


    for i in range(1, n + 1):
        if i in blocked_points:
            dp[i] = 0
        else:
            if i - 1 >= 0:
                dp[i] = dp[i - 1] + dp[i]


            if i - 2 >= 0:
                dp[i] = dp[i - 2]+ dp[i]


            if i - 3 >= 0:
                dp[i] = dp[i - 3]+ dp[i]

    return dp[n]

print(grasshopper_with_obstacles(2,[1]))
