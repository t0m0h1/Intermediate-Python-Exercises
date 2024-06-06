def greatest_common_divisor(n1, n2):
    """
    Calculates the greatest common divisor (GCD) of two numbers.

    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.

    Returns:
    int: The GCD of n1 and n2.
    """

    # Euclidean algorithm to find GCD
    while n2 != 0:
        # Update n1 to n2 and n2 to the remainder of n1 divided by n2
        n1, n2 = n2, n1 % n2

    return n1 # n1 is the GCD




def lowest_common_multiple(n1, n2):
    """
    Calculates the lowest common multiple (LCM) of two numbers.

    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.

    Returns:
    int: The LCM of n1 and n2.
    """


    # LCM of two numbers is the product of the two numbers divided by their GCD
    return n1 * n2 // greatest_common_divisor(n1, n2)




# driver code
if __name__ == '__main__':
    print(greatest_common_divisor(12, 18)) # 6
    print(lowest_common_multiple(12, 18)) # 36
