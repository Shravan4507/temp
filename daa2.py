# PS 2: Fractional Knapsack using Greedy Method
n = int(input("Enter number of items: "))

profit = list(map(int, input("Enter profits: ").split()))
weight = list(map(int, input("Enter weights: ").split()))

capacity = int(input("Enter knapsack capacity: "))

items = []

for i in range(n):
    ratio = profit[i] / weight[i]
    items.append((ratio, profit[i], weight[i]))

items.sort(key=lambda x: x[0], reverse=True)

total_profit = 0

for ratio, p, w in items:
    if capacity >= w:
        total_profit += p
        capacity -= w
    else:
        total_profit += ratio * capacity
        break

print("Maximum Profit:", total_profit)
