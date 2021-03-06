# Problem 8

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    k = len(L) - 1
    def f (x):
        value = 0
        for i in range(k+1):
            value += L[i]*(x**(k-i))
        return value
    return f
