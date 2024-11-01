print("Enter 3 numbers")
first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and second_number > third_number :
	print("Dereasing order")
elif third_number > second_number and second_number > first_number:
	print("Increasing order")
else:
	print("No particular order")
