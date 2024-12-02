"""
create an empty list
call it sorted numbers
prompt user to enter to enter 3 integers
append each entry to the list 
sort the list
print the sorted list
"""

sorted_numbers = []
first_number = input("Enter first number")
sorted_numbers.append(first_number)

second_number = input("Enter second number")
sorted_numbers.append(second_number)

third_number = input("Enter third number")
sorted_numbers.append(third_number)

sorted_numbers.sort()

print(sorted_numbers)


for number in sorted_numbers:
	print(number, end=",")
