def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the given number.
    
    Raises:
    ValueError: If the input is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
if __name__ == "__main__":
    test_number = 5
    result = factorial(test_number)
    print(f"The factorial of {test_number} is: {result}")