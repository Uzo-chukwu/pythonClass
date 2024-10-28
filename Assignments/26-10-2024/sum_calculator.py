iteration = 0
while iteration == 0:
    print("Enter 2 numbers.")
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    sum = first_number + second_number
    print(f"{first_number} + {second_number} = {sum}")

    iteration = int(input("Do you want to perform another addition? Enter 1 to continue or 0 to quit: "))