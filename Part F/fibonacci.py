def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test the function
n = 10
print(f"Fibonacci sequence up to the {n}th term:")
for i in range(n):
    print(fibonacci(i), end=" ")
print()