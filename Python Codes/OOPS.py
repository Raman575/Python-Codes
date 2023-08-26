from OOPS2 import  Menu, Restaurant
print("Welcome to Restaurant")
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
     dishes= {
        "momos": 100,
        "bullets": 60,
        "noodles": 150,
        "burger": 60,
        "fries": 40,
        "cola": 20,     
      }
     menu = Menu(title="Snacks", num_of_dishes=len(dishes)) 
     restaurant1 = Restaurant(name="The Pablo", phone_number="+91 99987 96325", address="Sarabha Nagar", rating="4.3", menu=menu)         
     restaurant1.show()
     print("DISHES:")
     print(dishes)          
     dishes_name = []
     quantities = []
     food_cart = []  # price
     while True:
        dish_name = input("Enter Dish Name to add in Cart: ")
        quantity = int(input("Enter Dish Quantity: "))
        dishes_name.append(dish_name)
        quantities.append(quantity)
        price = dishes[dish_name] * quantity
        food_cart.append(price)
        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break
     print(dishes_name)
     print(quantities)
     print(food_cart)
     amount = sum(food_cart)
     print("TOTAL AMOUNT: \u20b9", amount)
     message = """
        Welcome to Restaurant
        OFFERS FOR TODAY
        WELCOME50
        Get 50% OFF up to ₹100
        Valid on total value of items worth ₹159 or more.
        ZOMPAYTM
        Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
        Valid on total value of items worth ₹299 or more.
    """
     print(message)
     promo_code = input("Enter Promo Code: ")
     apply_promo_code(amount, promo_code)
if __name__ == "__main__":
    main()