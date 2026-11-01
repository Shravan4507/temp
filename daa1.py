# PS 1: Fibonacci Numbers and Step Count

n = int(input("Enter number of terms: "))

a, b = 0, 1
steps = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    steps += 1

print("\nStep Count:", steps)
