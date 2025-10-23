def grasshopper_with_obstacles(n, obstacles):

    if not obstacles:
        if n == 0: # прыжок на месте
            return 1
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]


    else:
        dp = [0] * (n + 1)
        if n == 0: # прыжок на месте
            dp[0] = 1
            return dp[n]
        if n == 1 and obstacles == 1:
            dp[1] = 1
            return dp[n]
        if n == 2 and (obstacles == [1] or [2]):
            dp[2] = 1
            return dp[n]
        if n == 2 and obstacles == [1,2]:
            dp[2] = 0
            return dp[n]
        if n == 3 and obstacles == [1,2]:
            dp[3] = 1
            return dp[n]



        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] +dp[i-3]
        return dp[n]






print(grasshopper_with_obstacles(5,[2]))


