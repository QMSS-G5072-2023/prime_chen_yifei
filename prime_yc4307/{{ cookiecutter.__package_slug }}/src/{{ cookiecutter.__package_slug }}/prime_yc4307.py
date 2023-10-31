import math

def is_prime(n):
    """
    Purpose: Check if a number is a prime number
    Input: Integer n
    Output: Bool value. True if is prime, False is not. 
    Example:
    is_prime(10)
    False
    """

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

