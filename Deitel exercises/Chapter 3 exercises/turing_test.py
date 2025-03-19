input("What is your problem:" )
response = input("Have you had this problem before? ").lower()
if response == "yes":
	print("Well you have it again")
elif response == "no":
	print("Well you have it now")
