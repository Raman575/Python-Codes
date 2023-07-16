"""
   Shopping cart
"""              
class Menu:
    def __init__(self, title, num_of_dishes):
        self.title = title
        self.num_of_dishes = num_of_dishes    
    def show(self):
        print("*********************")
        print("Title:", self.title)
        print("Num_of_dishes:", self.num_of_dishes)
        print("*********************")    
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