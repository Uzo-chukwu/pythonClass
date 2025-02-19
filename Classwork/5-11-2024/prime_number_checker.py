
def determine_prime(number):
    if number <= 1:
    	return False
    for digit in range(2, number):
    	if number % digit == 0:
        	return False
    return True

print(determine_prime(2))


"""
pseudocode

1. innitialize a fuction determine_prime 
2. set parameter to number
3. if number is less than 1 return false
4. create a for loop to iterate from 2 to value of number times 
5. let the iteration start from 2 to number-1
6. set the iterationv variable to digit
5. if number divides digit without remainder return false
6. return true if nothing divides number
"""