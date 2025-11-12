def min_coins(amount, coins):

    if not coins:
        return -1
    if amount == 0:
        return 0

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


print(min_coins(15, [1, 7, 10]))

