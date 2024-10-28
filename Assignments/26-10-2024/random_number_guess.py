while True:
    random_number = random.randint(1, 10)
    print("Pick a number from 1 to 10:")
    number = int(input())

    if number > random_number:
        print("Too high, try again.")
    elif number < random_number:
        print("Too low, try again.")
    else:
        print("You got it right!")
        break