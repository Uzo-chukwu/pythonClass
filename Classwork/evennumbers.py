largest= 0
count = 1
for count in range(11):
	score =int(input('Enter score from 1 to 100: '))
	if score > 0 and score <= 100:
		if score > largest:
			largest = score
	else:
		print('Invalid input! ')
		count+=1
print('The largest number is', largest)
		
