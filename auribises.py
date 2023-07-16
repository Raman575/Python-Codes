"""
(e-Learning Auribises)1 menu has many categories(Browse Courses, Success Stories, About Us)    
(Browse Courses, Success Stories, About Us) Many categories has Many sub-categories(Python, Typescript, Java)
(Python, Typescript, Java) Many sub-categories has Many Courses 
    """

class Menu:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def show(self):
        print(self.name, end=" | ")

    def show_categories(self):
        for category in self.categories:
            category.show()

class Course:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Rating:", self.rating)
        print("~~~~~~~~~~~~~~~~~~~")


class Category:
    def __init__(self, name, num_of_courses, num_of_learners, courses):
        self.name = name
        self.num_of_courses = num_of_courses
        self.num_of_learners = num_of_learners
        self.courses = courses

    def show(self):
        print("_____________________")
        print("Name:", self.name)
        print("Number of Courses:", self.num_of_courses)
        print("_____________________")

    def show_courses(self):
        for course in self.courses:
            course.show()