def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Test cases
print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print error message
print(divide(15, 3))  # Should print 5.0