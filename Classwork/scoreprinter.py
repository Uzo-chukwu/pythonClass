largest = 0 
validator = 1 

while validator <=10:
	score = int(input(f"enter number {validator}"))
	validator+=1
	if score > 0 and score <= 100:
		if score > largest:
			largest = score
	else:
		print('Invalid input! ')
		validator-=1
