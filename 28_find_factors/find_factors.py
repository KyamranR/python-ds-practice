def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []

    for nums in range(1, int(num**0.5) + 1):
        if num % nums == 0:
            factors.append(nums)

            if nums != num // nums:
                factors.append(num // nums)

    factors.sort()

    return factors