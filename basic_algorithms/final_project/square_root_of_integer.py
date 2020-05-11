def sqrt(number: int):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return sqrt_recursion(number, 0, number)


def sqrt_recursion(number, left, right):
    mid = (right + left) // 2
    if mid ** 2 <= number < (mid + 1) ** 2:
        return mid
    if number < mid * mid:
        return sqrt_recursion(number, left, mid - 1)
    return sqrt_recursion(number, mid + 1, right)


print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")
print("Pass" if (1 == sqrt(3)) else "Fail")
print("Pass" if (2 == sqrt(4)) else "Fail")
print("Pass" if (2 == sqrt(5)) else "Fail")
print("Pass" if (2 == sqrt(6)) else "Fail")
print("Pass" if (2 == sqrt(7)) else "Fail")
print("Pass" if (2 == sqrt(8)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
