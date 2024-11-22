number = int(input("Enter the number of rows and column: "))
astericks = "*"
second_astericks = "*****"

for i in range(0,number):
	
	print(astericks, second_astericks)
	astericks = astericks + "*"
	second_astericks = second_astericks - "*"
