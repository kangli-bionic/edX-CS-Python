#problem 4

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    maxList = []
    for i in t:
        if isinstance(i, int):
            maxList.append(i)
        else:
            maxList.append(max_val(i)) 
    return max(maxList)

print(max_val([[[[[[6]]]]]]))

