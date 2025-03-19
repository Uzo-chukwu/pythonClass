import math

def display_welcome_message():
    print("==========================================")
    print(" Welcome to Iya Moses Pizza Joint ")
    print("==========================================\n")

def get_number_of_guests():
    valid_input = False
    while not valid_input:
        try:
            number_of_guests = int(input("Enter the number of guests: "))
            if number_of_guests <= 0:
                print("Please enter a positive number.")
            else:
                valid_input = True
                return number_of_guests
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_pizza_choice():
    pizza_types = ["Sapa size", "Small Money", "Big boys", "Odogwu"]
    slices_per_box = [4, 6, 8, 12]
    price_per_box = [2500, 2900, 4000, 5200]

    print("\nAvailable Pizza Types:")
    for i in range(len(pizza_types)):
        print(f"{i + 1}. {pizza_types[i]} - {slices_per_box[i]} slices, ₦{price_per_box[i]} per box")

    valid_input = False
    while not valid_input:
        try:
            choice = int(input("\nSelect your pizza type (1-4): "))
            if 1 <= choice <= 4:
                valid_input = True
                return choice - 1
            else:
                print("Invalid pizza type selected. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def process_order(number_of_guests, pizza_choice):
    pizza_types = ["Sapa size", "Small Money", "Big boys", "Odogwu"]
    slices_per_box = [4, 6, 8, 12]
    price_per_box = [2500, 2900, 4000, 5200]

    selected_pizza = pizza_types[pizza_choice]
    slices_per_box_for_type = slices_per_box[pizza_choice]
    price_per_box_for_type = price_per_box[pizza_choice]

    total_boxes = math.ceil(number_of_guests / slices_per_box_for_type)
    total_slices = total_boxes * slices_per_box_for_type
    leftover_slices = total_slices - number_of_guests
    total_price = total_boxes * price_per_box_for_type

    print("\nOrder Summary:")
    print(f"Pizza Type: {selected_pizza}")
    print(f"Number of boxes to buy: {total_boxes} boxes")
    print(f"Leftover slices: {leftover_slices} slices")
    print(f"Total price: ₦{total_price}")

def display_goodbye_message():
    print("\n==========================================")
    print(" Thank you for choosing Iya Moses Pizza! ")
    print(" Enjoy your party and the pizza! ")
    print("==========================================")

def main():
    display_welcome_message()
    number_of_guests = get_number_of_guests()
    pizza_choice = get_pizza_choice()
    process_order(number_of_guests, pizza_choice)
    display_goodbye_message()

main()