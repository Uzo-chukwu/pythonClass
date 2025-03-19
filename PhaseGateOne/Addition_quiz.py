"""
import random
generate a random number between 1 and 100
save it as first number
generate a random number between 1 and 100
save it as second number
add up first number and second number 
save as answer
ask the user to provide the sum of first number and second number
if the user's inut is same as answer print true
else print false
"""

import random

first_number = random.randint(1,100)
second_number = random.randint(1,100)
answer = first_number + second_number
print(first_number," + ",second_number, " = ____ ")
user_input = int(input("Enter your answer:"))

if user_input == answer:
	print("True")
else:
	print("False")