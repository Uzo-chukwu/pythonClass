principal=int(input('Enter the principal amount: '))

annual_rate = int(input('Enter the annual interest rate: '))

years = int(input('Enter the duration in years: '))

monthly_rate = (annual_rate/100)/12

months = years * 12

monthly_payment = principal*((monthly_rate*(1+monthly_rate)**months)/(((1+monthly_rate)**months)-1))

monthly_payment = monthly_payment//1

print('Your monthly payment is', monthly_payment)