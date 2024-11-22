

def get_number(numbers):
	
	summed = 0
	for i in range(len(numbers)):
		summed += (sum(numbers) - numbers[i])
	return summed

	
def merge_and_sort(number1,number2):
	
	numbers = number1 + number2
	
	numbers.sort()
	return numbers	

def getvowels(strings):
	strings = strings.lower()
	totalvowels = 0
	for alphabet in strings:
		if alphabet in 'aeiou':
			totalvowels += 1
	return totalvowels

def getanagram(first,second):
	first.lower()
	second.lower()
	numberofsamealphabet = 0
	if len(first) != len(second):
		return "false"
			
	else:
		for letter in first:
			for alpha in second:
				if letter == alpha:
					numberofsamealphabet += 1
	if numberofsamealphabet == len(first):
		return "True"

def getevennumber(numbers):
	totaleven = 0
	for number in numbers:
		if number % 2 == 0:
			totaleven += number
	return totaleven
			
def getprime(number):
	primecounter = 0
	if number <= 1:
		return False
	for i in range(2,number):
		if number % i == 0:
			primecounter += 1
	if primecounter == 0:
		return True
	else: return False
		
def getpalindrome(string):
	string = string.lower().replace(" ", "")  
	pal = string[::-1]
	if pal == string:
		return True
	else:
		return False
	
def getaverage(numbers):
	return sum(numbers)/ len(numbers)

def getreverse(string):
	 return string[::-1]

def getuppercase(string):
	for i in range(len(string)):
		string[i] = string[i].capitalize()

	return string
def getduplicate(numbers):
	count = 0
	for number in range(len(numbers)):
		if numbers[number] in numbers:
			count += 1
	
	if count > 1:
		return True
	elif count <= 1:
		return False

def removespace(string):
	return string.replace(' ','')
		 
def getcommonnumber(list1,list2):
	common_numbers=[]
	for number in list1:
		if number in list2:
			common_numbers.append(number)
	return common_numbers
def sortstring(string):
	return sorted(string, key=len)

def getfactorial(number):
	result = 1
	for count in range(1,number+1):
		result *= count
	return result 

def getsumofdigits(number):
	sumofdigits = 0
	for digit in str(number):
		sumofdigits += int(digit)
	return sumofdigits

def getsumofodddigits(number):
	
	sumofodddigits = 0
	for digit in str(number):
		if int(digit) % 2 != 0:
			sumofodddigits += int(digit)
	return sumofodddigits

def getacronym(phrase): 
	words = phrase.split()
	acronym = ''.join(word[0].upper() for word in words)
	return acronym			
		
