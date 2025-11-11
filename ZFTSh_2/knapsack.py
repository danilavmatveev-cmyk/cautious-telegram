def knapsack(weights, values, capacity):
    dp = [[0]*(capacity+1) for _ in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        for j in range (1,capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - weights[i-1]])
            else:
                dp[i][j] = dp[i - 1][j]



    selected_items = []
    i, j = len(weights), capacity

    while i > 0 and j > 0:

        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1
    return dp[len(weights)][capacity], list(reversed(selected_items))


print(knapsack([1, 2,3], [10, 15, 40], 5))
