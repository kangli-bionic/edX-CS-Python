#problem 3

def sum_digits(s):
    """ 
    assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception. 
    """
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sum = 0
    for i in s:
        if i in digits:
           sum += int(i)
    if sum == 0 and str(0) not in s:
        raise ValueError
    return sum

print(sum_digits("0"))