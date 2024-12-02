"""
import random
generate a random number from 0 to 1000
create a function that gets the sum of the digits in an integer
call the function and give it the random numberas argument
print result
"""



import random
random_number = random.randint(0,1000)

def get_sum_of_digits(number):
	return sum([int(num) for num in str(number)])



sum_of_digits = get_sum_of_digits(random_number)

print("The sum of the digits in ", random_number,"is", sum_of_digits)
