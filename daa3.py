# 0/1 Knapsack using Dynamic Programming


n = int(input("Enter number of items: "))

profit = list(map(int, input("Enter profits: ").split()))
weight = list(map(int, input("Enter weights: ").split()))

capacity = int(input("Enter knapsack capacity: "))

dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weight[i - 1] <= w:
            dp[i][w] = max(
                profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit:", dp[n][capacity])
