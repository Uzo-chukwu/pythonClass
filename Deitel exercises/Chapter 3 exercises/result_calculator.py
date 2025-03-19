passes = 0
fails = 0
students = 1

while students < 11 :
	result = int(input("Enter result, (1=pass 2=fail): "))
	if result == 1:
		passes +=1
	elif result == 2:
		fails +=1
	else:
		students += 1
		continue
	students+=1
		

print(passes ,"passed", fails ,"failed")
if passes > 7:
	print("Bonus for facilitator")

	
