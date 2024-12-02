"""
import random
create a variable called scorecount
initialize a for loop to run 10 times
generate a random number from 50 to 100 
save as random number one
generate a random number from 0 to 50 
save as random number two
calculate random number one - random number two
save result as answer
promp user to enter the result of random number one - random number two
save as userinput
if user input is = answer print correct and add one to scorecount 
else print wrong 
end loop
print score
"""

import random
score_count = 0
for count in range(10):
	random_number_one = random.randint(50,100)
	random_number_two = random.randint(0,50)
	answer = random_number_one - random_number_two
	print(random_number_one, '-' , random_number_two)
	user_input = int(input("Enter your answer:"))
	if user_input == answer:
		print("Correct!")
		score_count+= 1
	else:
		print("Wrong!")

print("Your score is ",score_count,"/ 10")

