number = int(input('Enter a number between 0 and 1000'))
firstnumber = number//100
secondnumber = (number//10)//10
thirdnumber = number%10

sum=firstnumber+secondnumber+thirdnumber
print('The sum of the digits is', sum)