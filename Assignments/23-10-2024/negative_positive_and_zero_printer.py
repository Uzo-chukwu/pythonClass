negative = 0
positive = 0
zero = 0

for count in range(5):
	number = int(input("Enter a number: "))
	if number < 0:
		negative+=1
	elif number == 0:
		zero+=1
	else:
		positive+=1
print('negative=',negative   ,'zero=',zero,  'positive=', positive)
	
	