import math
def divide_or_square(number):
	if number % 5 == 0:
		return math.sqrt(abs(number))
	else:
		return number % 5
def get_future_investment_value (investment_amount, monthly_interest_rate, years):

	number_of_months =  years * 12
	future_investment_amount = investment_amount * (1 + monthly_interest_rate)**number_of_months
	
	return future_investment_amount

	

def get_only_floats(a,b):
	if a % 1 != 0 and b % 1 != 0 :
		return 2
	elif (a % 1 != 0 and b % 1 == 0) or (a % 1 == 0 and b % 1 != 0):
		return 1
	else:
		return 0






