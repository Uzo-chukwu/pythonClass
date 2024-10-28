


largest = float('-inf')
smallest = float('inf')

while True:
    num_input = input("Enter a number or enter '-1' to quit: ")
    number = int(num_input)
    
    if number == -1:
        break
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

if largest != float('-inf') and smallest != float('inf'):
    print(f"The smallest number is {smallest}\nThe largest number is {largest}")
else:
    print("No valid input entered")