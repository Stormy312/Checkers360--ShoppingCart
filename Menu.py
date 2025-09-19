"""
Checkers360 Shopping Cart application
SSX362 - Assignment 2
Thabo Sibeko 
"""
def checkout(cart): # checkout method also main exit of application
    print("\n--- Checkout ---")
    if not cart:
        print("Your cart is empty")
    else:
        total = sum(details["price"] * details["quantity"] for details in cart.values())
        print(f"Final Total: R{total:.2f}")
    print("Thank you for shopping at Checkers360! Proceeding to checkout...")

def view_cart(cart): #  the view method
    if not cart: # this is for empty cart dict/ no items
        print("No cart")
        return

    print("\n--- Your Cart ---\n")
    total = 0
    for item, details in cart.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f"{item}: R{details['price']: .2f} x {details['quantity']} = R{item_total: .2f}")
    print(f"Total Cart Value: R{total: .2f}")
    # Output should see each item, price, quantity and the running total


def add_item(cart): #the add item Method
    item = input("Enter item name: ").capitalize()
    try:
        price = float(input(f"Enter price for {item}: R "))
        quantity = int(input(f"Enter quantity of {item}: "))
    except ValueError: # Error handling for the Menu
        print("Invalid input of price and quantity must be integers. ")
        return

    if item in cart:
        cart[item]["quantity"] += quantity # Update if it already exists item
        print(f"Update {item}, new quantity: {cart[item]['quantity']}")
    else:
        cart[item] = {"price": price, "quantity": quantity}
        print(f"Added {item} to cart")



def main(): #Main Interface
    cart = {} # empty dict to keep adding items

    while True:
        print("\n --- Checker360 Shopping Cart ---")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Checkout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            checkout(cart)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()