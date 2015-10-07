# Calculates simple exponents
# by exvxs

p = input('Enter a whole number: ')
q = input('Enter second whole number: ')
def exponent(p): # prints the exponent of a number
    exponented = p**q
    print '%d to the power of %d becomes %d' % (p, q, exponented)
    return exponented
exponent(p)
