#Number base direct conversion 
#Code from Stack exchange
#Reference: https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base


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

def convertNumberToList(number):
	number = str(number)
	List = []
	for item in number:
		List.append(int(item))
	return List

def convertListToNumber(List):
	return int(''.join(str(item) for item in List))

def convertToBase(number, incomingBase, outgoingBase):
    """Convert the digits representation of a number from base b to base c."""
    return convertListToNumber(toDigits(fromDigits(convertNumberToList(number), incomingBase), outgoingBase))





def returnPhoneNumber():
	return "Shuvo: 01929571838"
