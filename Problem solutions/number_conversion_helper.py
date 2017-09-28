#Number base direct conversion 
#Code from Stack exchange
#Reference: https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base
#Reference function/s 1 Starts here

def toDigits(n, b):
    """Convert a positive number n to its digit representation in base b."""
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    return digits

def fromDigits(digits, b):
    """Compute the number given by digits in base b."""
    n = 0
    for d in digits:
        n = b * n + d
    return n

def convertBase(digits, b, c):
    """Convert the digits representation of a number from base b to base c."""
    return toDigits(fromDigits(digits, b), c)

#Reference function/s 1 ends here 
