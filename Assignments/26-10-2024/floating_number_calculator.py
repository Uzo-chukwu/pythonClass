first_number = float(input("Enter first decimal number: "))

second_number = float(input("Enter second decimal number: "))

first_float = first_number % 1
second_float = second_number % 1

rounded_first = round(first_float, 3)
rounded_second = round(second_float, 3)

if rounded_first == rounded_second:
print("They are the same!")
else:
print("They are not the same!")