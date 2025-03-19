def is_palindrome(number):
    str_number = str(number)
    left = 0
    right = len(str_number) - 1
    while left < right:
        if str_number[left] != str_number[right]:
            return False
        left += 1
        right -= 1
    return True



def get_sum_of_even_numbers(numbers):
	sum_of_even = 0
	for number in numbers:
		if number % 2 == 0:
			sum_of_even += number
	return sum_of_even

def is_prime_number(number):
    if number <= 1:
        return False
    prime_counter = 0
    for count in range(number, 1, -1):
        if number % count == 0:
            prime_counter += 1
    if prime_counter == 1:
        return True
    return False



def get_prime_number_before(number):
	prime_numbers = []
	for count in range(2,number):
		number_is_prime = is_prime_number(count)
		if(number_is_prime):
			prime_numbers.append(count)

	return prime_numbers
def list_of_five():
	my_list = []
	for i in range(1,6):
		numbers.append(i)
	return my_list
def get_even_number_count(numbers):
	return len([number for number in numbers if number % 2 == 0 ])


def get_boolean_value(numbers):
	return[number % 2 == 0 for number in numbers]


def capitalize_first_Letter(phrase):
	return[word.capitalize() for word in phrase]

def multiple_of_three(number):
	return[num for num in range(3,number+1,3) ]
def square_odd_numbers(numbers):
	return[number ** 2 for number in numbers if number % 2 != 0]
 
def sqaure_numbers_before(number):
	return[num**2 for num in range(1,number+1)]

def get_numbers_greater_than_ten(numbers):
	return list(filter(lambda num : num > 10, numbers))

def check_palindrome(words):
	return list(map(lambda s: s == s[::-1], words))

def get_int(nonsense):
	return [int(num) for num in nonsense]

def get_n_letter_words(words,number):
	return list(filter(lambda words: len(words) >= number, words))



#list(filter(lambda s: s.isdigit(), nonsense))

def add_up(number):
	#return sum([int(num) for num in str(number) ])
	return sum(list(map(lambda num: int(num), str(number))))

def remove_vowels(words):
	return [word.pop('a'or'e'or'i'or'o'or'u') for word in words]

def get_even_dict(number):
	return{x:x for x in range(2,number,2)}

def pair_up_list(keys,values):
	return dict(zip(keys, values))

def get_dict_values(diction):
	return [value for value in diction.values()]
def swap_key_to_values(diction):
	return 




