
import math

def get_largest_element(numbers):
    largest = float('-inf')
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def reverse_list(numbers):
    reverse_numbers = [0] * len(numbers)
    for count in range(len(numbers) - 1, -1, -1):
        reverse_numbers[len(numbers) - 1 - count] = numbers[count]
    return reverse_numbers

def check_element(number, numbers):
    for digit in numbers:
        if number == digit:
            return True
    return False

def print_odd_position(numbers):
    for count in range(len(numbers)):
        if count % 2 != 0:
            print(numbers[count], end=" ")

def print_even_position(numbers):
    even_element = [0] * len(numbers)
    for count in range(len(numbers)):
        if count % 2 == 0:
            print(numbers[count], end=" ")

def get_running_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def check_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    return word == reversed_word

def get_sum_of_numbers_for(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def get_sum_of_numbers_while(numbers):
    total = 0
    count = 0
    while count < len(numbers):
        total += numbers[count]
        count += 1
    return total

def get_sum_of_numbers_do_while(numbers):
    total = 0
    count = 0
    while True:
        total += numbers[count]
        count += 1
        if count >= len(numbers):
            break
    return total

def concatenate_list(letters, numbers):
    combined = [0] * (len(letters) + len(numbers))
    for count in range(len(letters)):
        combined[count] = letters[count]
    for count in range(len(numbers)):
        combined[count + len(letters)] = numbers[count]
    return combined

def concatenate_list_alternatively(letters, numbers):
    combined = [0] * (len(letters) + len(numbers))
    for count in range(len(letters)):
        combined[count] = letters[count]
    for count in range(len(numbers)):
        combined[count + len(letters)] = numbers[count]
    return combined

def get_list_of_digits(number):
    list_of_digits = [0] * len(str(number))
    counter = len(str(number)) - 1
    while number > 0:
        list_of_digits[counter] = number % 10
        number //= 10
        counter -= 1
    return list_of_digits

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

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

def subtract(first_number, second_number):
    return abs(first_number - second_number)

def divide(dividend, divisor):
    if divisor == 0:
        return 0
    return dividend / divisor

def factor_of(number):
    count = 0
    for digit in range(1, number + 1):
        if number % digit == 0:
            count += 1
    return count

def is_square(number):
    square_root = math.sqrt(number)
    return square_root * square_root == number

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

def factorial_of(number):
    result = 1
    for digit in range(2, number + 1):
        result *= digit
    return result

def square_of(number):
    return number * number