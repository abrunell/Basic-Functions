def getValue():
	"""
	Reads an input from the console and returns it.

	"""
	return input('Enter an integer: ')


def validateValue(value):
	""" (input) -> boolean

	Validate that value is an integer and return true or false

	>>> validateValue(402)
	True
	>>> validateValue('banana')
	False

	"""
	try:
		value = int(value)
		if isinstance(value,int):
			return True
	except:
		return False
	    

def findArea(length, width):
	""" (int, int) -> int

	Checks that length and width are validated as integers
	and returns the product of length * width.

	>>>findArea(50, 3)
	150
	>>>findArea(4, 12)
	48
	>>>finaArea('banana', 20)
	-1
	"""
	if validateValue(length) and validateValue(width):
		return int(length) * int(width)
	else:
		return -1
