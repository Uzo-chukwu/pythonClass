weight=float(input('Enter your weight in kilogram'))

height=float(input('Enter your height in meters'))

bmi=weight/(height**2)

print('Your BMI is', round(bmi, 1))

if bmi < 18.5:
	print('You are underweight: ')
elif bmi > 18.5 and bmi < 25:
	print('You weight is normal ')
elif bmi > 25 and bmi < 30:
	print('You are overweight')
else:
	print('You are obese')




