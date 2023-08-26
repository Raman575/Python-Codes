
#relationship mapping
# 1 restaurant has 1 menu
#Many menu has many dishes
"""
dishes-name, price , rating
menu - title, num_of_dishes, dishes
restaurant - name, phone_number, address, rating, menu
"""

class Dish:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price 
        self.rating = rating
        
    def show(self):
        print("~~~~~~~~~~~~~~~~~~")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Rating:", self.rating)
        print("~~~~~~~~~~~~~~~~~~")
        
                
class Menu:
    def __init__(self, title, num_of_dishes, dishes):
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes
        
    def show(self):
        print("*********************")
        print("Title:", self.title)
        print("Num_of_dishes:", self.num_of_dishes)
        print("*********************")
        
        for dish in self.dishes:
            dish.show()  
              
class Restaurant:
    def __init__(self, name, phone_number, address, rating, menu):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.rating = rating
        self.menu = menu
        
    def show(self):
        print("________________________")
        print("Name:", self.name)
        print("Phone number:", self.phone_number)
        print("Address:", self.address)
        print("Rating:", self.rating)
        print("________________________")
        
        self.menu.show()
         
            
def main():
    dish1 = Dish(name="Momos", price="150", rating="4.9")
    dish2 = Dish(name="Noodles", price="250", rating="4.5")
    dish3 = Dish(name="Burger", price="100", rating="4.0")
    dish4 = Dish(name="Chaap", price="180", rating="4.3")
    dish5 = Dish(name="Pizza", price="300", rating="4.9")
    
    dishes = [dish1, dish2, dish3, dish4, dish5]
    
    menu = Menu(title="Snacks", num_of_dishes=len(dishes), dishes=dishes)
    
    restaurant1 = Restaurant(name="The Pablo", phone_number="+91 99987 96325", address="Sarabha Nagar", rating="4.3", menu=menu)
    
    restaurant1.show()

if __name__ == "__main__":
    main()
    