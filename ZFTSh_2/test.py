def grasshopper_with_obstacles(n, obstacles):
    if n < 0:
        return 0


    blocked_obs = set(obstacles)

    #
    dp = [0] * (n + 1)


    if 0 in blocked_obs:
        return 0
    else:
        dp[0] = 1

    # Заполняем массив dp для клеток от 1 до n
    for i in range(1, n + 1):
        if i in blocked_obs:
            dp[i] = 0
        else:
            # Прыжок на +1
            if i - 1 >= 0:
                dp[i] += dp[i - 1]

            # Прыжок на +2
            if i - 2 >= 0:
                dp[i] += dp[i - 2]

            # Прыжок на +3
            if i - 3 >= 0:
                dp[i] += dp[i - 3]

    return dp[n]






print(grasshopper_with_obstacles(3,[2]))


