n = int(input("Enter number of items: "))
capacity = float(input("Enter knapsack capacity: "))
items = []
for i in range(n):
    weight = float(input(f"Enter weight of item {i+1}: "))
    value = float(input(f"Enter value of item {i+1}: "))
    items.append((weight, value))
items.sort(key=lambda x: x[1] / x[0], reverse=True)
total_value = 0
for weight, value in items:
    if capacity <= 0:
        break
    if weight <= capacity:
        total_value += value
        capacity -= weight
    else:
        fraction = capacity / weight
        total_value += value * fraction
        capacity = 0
print("\nMaximum value:", total_value)