def grasshopper_with_obstacles(n, obstacles):

    if not obstacles:
        if n == 0:
            return 1
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i-3]
        return dp[n]
    else:
        if n == 0:
            return 1
        if n == 1:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]






print(grasshopper_with_obstacles(4,[3]))


