message ="""Enter 1 for Breakfast
Enter 2 for Lunch
Enter 3 for Dinner :"""

option = int(input(message))

match option:
	case 1:
		print("Breakfast")
	case 2:
		print("lunch")
	case 3:
		print("dinner")