"""
(e-Learning Auribises)1 menu has many categories(Browse Courses, Success Stories, About Us)    
(Browse Courses, Success Stories, About Us) Many categories has Many sub-categories(Python, Typescript, Java)
(Python, Typescript, Java) Many sub-categories has Many Courses 
    """

class menu:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
        
        def show(self):
            print("*****************")
            print(self.name, end="|")
            print("*****************")
            
            
                

class course:
     def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
     def show(self):
            print("~~~~~~~~~~~~~~~~~~~")
            print("name:", self.name)
            print("price:", self.price)
            print("rating:", self.rating)
            print("~~~~~~~~~~~~~~~~~~~")
             
class category:
    def __init__(self, name, num_of_courses, num_of_learners):
        self.name = name
        self.num_of_courses = num_of_courses
        self.num_of_learners = num_of_learners
        def show(self):
            print("_____________________")
            print("name:", self.name)
            print("num_of_courses:", self.num_of_courses)
            print("num_of_learners:", self.num_of_learners)
            print("_____________________")
            

