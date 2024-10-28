while True:
    alphabet = input("Enter an alphabet: ")
    length = len(alphabet)
    
    if length != 1:
        print("You made a wrong input. Please enter a single alphabet.")
        continue
    
    if alphabet.upper() in 'AEIOU':
        print("You entered a vowel")
    else:
        print("You entered a consonant")
        stopper = int(input("Do you want to continue after this? Enter 0 to quit or 1 to continue: "))
        if stopper == 0:
            break