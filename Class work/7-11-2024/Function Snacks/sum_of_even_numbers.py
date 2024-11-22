
def sum_of_even_numbers(number):
	sum = 0
	for value in range(0,number+1,2):	
		sum += value
	return sum


digit = sum_of_even_numbers(int(input("Enter a number: ")))
print(digit)