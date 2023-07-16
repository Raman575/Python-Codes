def apply_promo_code(amount, promo_code):
    if promo_code == "WELCOME50":
        if amount >= 159:
            print("Promo Code Applied Successfully...")

            discount = 0.50 * amount

            if discount >= 100:
                discount = 100

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)

    elif promo_code == "ZOMPAYTM":
        if amount >= 299:
            print("Promo Code Applied Successfully...")

            discount = 0.20 * amount

            if discount >= 50:
                discount = 50

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
            print("You will get a cashback of: \u20b9 25")
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)
    else:
        print("Promo Code Invalid")
        print("Please Pay: \u20b9", amount)

def main():
    menu = {
        "momos": 100,
        "bullets": 60,
        "noodles": 150,
        "burger": 60,
        "fries": 40,
        "cola": 20,     
    }
    
    print("MENU")
    print(menu)
    
    item_name = []  # name of food
    quantities = []  # quantity of food
    food_cart = []  # price
    
    while True:
        item_names = input("Choose the dish from menu:")
        quantity = int(input("Enter quantity of food:"))
        item_name.append(item_names)
        quantities.append(quantity)
        price = menu[item_names] * quantity
        food_cart.append(price)
        
        choice = input("Do you want to add more to cart? (yes/no)")
        if choice == "no":
            break
        
    print(item_name)
    print(quantities)
    print(food_cart)
        
    amount = sum(food_cart)
    print("Amount to pay: \u20b9", amount)
    
    message = """
    TODAY OFFER's 
    Use code - WELCOME50 
    You will get 50% discount upto ₹100.
    Valid on total value of items worth ₹159 or more.
    
    Use code - ZOMPAYTM 
    You will get 20% discount upto ₹50 and ₹25 Paytm cashback using Paytm.
    Valid on total value of items worth ₹299 or more.
    """
    print(message)
    promo_code = input("Enter Promo code for discount:")
    apply_promo_code(amount, promo_code)    
if __name__ == "__main__":
    main()
