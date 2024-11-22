
number = int(input("Enter a number"))

remainder = 0
sum = 0

while number > 0:

	remainder = number % 10
	if remainder >= 5:
		sum += 1
	number//= 10

	
print (sum)