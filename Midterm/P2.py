#Problem 5

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    newString = ""
    for i in s: 
        if i.lower() not in vowels: 
            newString += i
    print(newString)

