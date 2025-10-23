def grasshopper_with_obstacles(n, obstacles):
    if not obstacles:
        if n == 0:  # прыжок на месте
            return 1
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        if n >= 2:
            dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
    else:
        dp = [0] * (n + 1)

        # Инициализация для позиции 0
        if 0 < len(obstacles) and obstacles[0] == 1:
            dp[0] = 0
        else:
            dp[0] = 1

        # Инициализация для позиции 1
        if n >= 1:
            if 1 < len(obstacles) and obstacles[1] == 1:
                dp[1] = 0
            else:
                # На позицию 1 можно попасть только с позиции 0
                dp[1] = dp[0]

        # Инициализация для позиции 2
        if n >= 2:
            if 2 < len(obstacles) and obstacles[2] == 1:
                dp[2] = 0
            else:
                # На позицию 2 можно попасть с позиций 0 и 1
                dp[2] = dp[0] + dp[1]

        # Заполнение для остальных позиций
        for i in range(3, n + 1):
            if i < len(obstacles) and obstacles[i] == 1:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]


print(grasshopper_with_obstacles(2, [2]))