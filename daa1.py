n = int(input("Enter the number of terms: "))
a, b = 0, 1
steps = 1
print("\nIterative Fibonacci Series:")
for i in range(n):
    steps += 1
    print(a, end=" ")
    a, b = b, a + b
    steps += 3
steps += 1
print("\nIterative Step Count:", steps)
recursive_steps = 0
def fibonacci(k):
    global recursive_steps
    recursive_steps += 1
    if k <= 1:
        return k
    return fibonacci(k - 1) + fibonacci(k - 2)
print("\n\nRecursive Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")
print("\nRecursive Step Count (function calls):", recursive_steps)