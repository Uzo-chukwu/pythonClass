
number = int(input("Enter 5 digits number: "))
modulo = 10000

for i in range(0,5):

	print(number)
	number%=modulo
	modulo//=10
	


