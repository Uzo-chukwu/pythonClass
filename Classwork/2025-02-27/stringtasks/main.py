

def character_frequency(string):
    frequency ={}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def swap_first_last(letter):
    if len(letter) <= 1:
        return letter
    return letter[-1] + letter[1:-1] + letter[0]


def merge_and_swap(string1, string2):
    swapped_str1 = swap_first_last(string1)
    swapped_str2 = swap_first_last(string2)
    return f"{swapped_str1} {swapped_str2}"

def put_ce_in_the_middle(string):

    new_string = ""
    words = string.split()
    mid_position = len(words) // 2
    first_half = ""
    second_half = ""
    for count in range(mid_position,len(words)):
        second_half += string[count]
    for count in range(mid_position):
        first_half += string[count]
    if len(string) % 2 != 0:
        new_string = string + "ce"
    else:
        new_string = first_half + "ce" + second_half
    return new_string


def uppercase_first(string):
    new_string = ""
    for char in string:
         if char.isupper(): new_string += char.upper()
    for char in string:
        if char.islower(): new_string += char.lower()
    return new_string

def get_number_of_occurences(string,character):
    my_tuple = ()
    count = 0
    for char in string:
        if char == character:
            count += 1
    my_tuple = [character, count]
    return my_tuple

def removespecial_characters(string):
    new_string = ""
    for char in string:
        if char.isalpha() or char.isdigit():
            new_string += char
    return new_string



print(put_ce_in_the_middle())
def get_even_number(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers





