


for count in range(1,15):

	pass = 0
	fail = 0
	score = 0
	score = int(input("Enter the student", count,"'s score"))
	if score >= 45:
		pass += 1
	elif score < 45:
		fail += 1

print("number of failed student =", fail)

print("number of passed student =", pass)