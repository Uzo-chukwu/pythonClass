
def calculate_total(cart):
    total = 0
    for product in cart:
        total += product['price'] * product['quantity']
    return total

def calculate_discount(total, discount_rate):
    if total >= 100:
        return total * discount_rate
    else:
        return 0

def calculate_vat(total, discount):
    return (total - discount) * 0.075

def display_invoice(cart, total, discount, vat, grand_total):
    print("Product Name | Quantity | Unit Price | Subtotal")
    for product in cart:
        subtotal = product['price'] * product['quantity']
        print(f"{product['name']} | {product['quantity']} | {product['price']} | {subtotal}")
    print(f"Total Price: {total}")
    print(f"Discount: {discount}")
    print(f"VAT: {vat}")
    print(f"Grand Total: {grand_total}")

def process_payment(grand_total):
    payment = float(input("Enter payment amount: "))
    if payment >= grand_total:
        balance = payment - grand_total
        print(f"Payment successful. Balance: {balance}")
    else:
        print("Insufficient payment. Please complete payment.")

def main():
    cart = []
    active = True 
    while active:
        print("1. Add product to cart")
        print("2. Checkout")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            cart.append({'name': name, 'price': price, 'quantity': quantity})
        elif choice == "2":
            total = calculate_total(cart)
            discount_rate = 0.1
            discount = calculate_discount(total, discount_rate)
            vat = calculate_vat(total, discount)
            grand_total = (total - discount) + vat
            display_invoice(cart, total, discount, vat, grand_total)
            process_payment(grand_total)
            cart.clear()
        elif choice == "3":
            active = alse
        else:
            print("Invalid choice. Please try again.")

main()