def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that us reversed of input
    """

    if len(input) <= 1:
        return input
    else:
        output = input[-1] + reverse_string(input[:-1])
        return output


print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
