
number = int(input("Enter a number"))

remainder = 0
sum = 0

while number > 0:

	remainder = number % 10
	sum += remainder
	number//= 10

	
print (sum)