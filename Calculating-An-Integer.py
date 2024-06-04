def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is defined for non-negative integers.")
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
# result = factorial(5)  # Calculates 5!


