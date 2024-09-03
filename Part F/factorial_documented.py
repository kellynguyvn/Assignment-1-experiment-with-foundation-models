def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    The factorial of n, denoted as n!, is the product of all positive integers
    less than or equal to n. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        n (int): A non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.

    Raises:
        RecursionError: If n is too large, causing maximum recursion depth to be exceeded.
        ValueError: If n is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(10)
        3628800

    Note:
        This function uses recursion to calculate the factorial.
        For very large values of n, consider using an iterative approach
        or math.factorial() to avoid recursion depth issues.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be a non-negative integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
if __name__ == "__main__":
    print(factorial(5))  # Should print 120
    print(factorial(0))  # Should print 1
    try:
        print(factorial(-1))  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(factorial(1000))  # May raise RecursionError
    except RecursionError as e:
        print(f"Error: {e}")