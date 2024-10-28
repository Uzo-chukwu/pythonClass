
number = int(input("Enter a number:"))

print("Enter the number of terms:")
number_of_terms = int(input())

counter = 0
while counter <= number_of_terms:
    print(f"{number} * {counter} = {number * counter}")
    counter += 1