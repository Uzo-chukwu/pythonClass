number_of_days = int(input("Enter the number of days: "))

if number_of_days <= 5:
	print("50 paise fine") 
elif number_of_days > 5 and number_of_days <11:
	print("1 rupee fine")
elif number_of_days > 10 and number_of_days <30:
	print("5 rupees fine")
elif number_of_days >=30:
	print("Membership cancelled")