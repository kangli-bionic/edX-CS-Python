#Midterm Problem 4

# A triangular number is a number obtained by the continued summation of integers starting from 1. 
# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not 
    """
    m = 1
    while True:
        if n == 0:
            return True
        elif n > 0:
            n -= m
            m += 1
        else:
            return False


