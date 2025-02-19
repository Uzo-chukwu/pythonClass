print("hello")
def get_sum(numbers):
	
	total = 0
	for number in numbers:
		total += number

	return total
		

def remove_function(numbers):
	
	if len(numbers) > 1:	
		numbers.pop(2)
	else:
		return 0
			
	return numbers

