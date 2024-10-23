number=int(input('Enter a three digit integer: '))

firstinteger=number//100
lastinteger=number%10

palindrome = firstinteger /lastinteger

if palindrome == 1:
	print(number, 'Is a palindrome')
else:
	print(number, 'Is not a palindrome')