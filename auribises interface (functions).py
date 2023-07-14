from auribises import course, category, menu
"""
(e-Learning Auribises)1 menu has many options(Browse Courses, Success Stories, About Us)    
(Browse Courses, Success Stories, About Us) One option has Many sub-categories(Python, Typescript, Java)
(Python, Typescript, Java) Many sub-categories has Many Courses 
    """
    
def main():
    
    Python_courses = [
        course(name="Python for kids", price="3000", rating="4.5")
              ]
    [
        course(name="Python with data science", price="12000", rating="4.9")
    ]
    [
        course(name="Programming with Java SE", price="12000", rating="4.9")
    ]         
    [
        course(name="Full Stack Development", price="16000", rating="4.8")
              ]
    
    Typescript_courses = [
        course(name="Typescript", price="10000", rating="4.5")
              ]
    [
        course(name="App Development with Flutter", price="9000", rating="4.9")
    ]
    
    Java_courses = [
        course(name="Java J2EE & SOA", price="16000", rating="4.9")
              ]
    [
        course(name="App Development with Flutter", price="9000", rating="4.9")
    ]
    
    
    
    categories = category(name="Python", num_of_courses="4", num_of_learners="593")
    categories = category(name="Typescript", num_of_courses="0", num_of_learners="0")
    categories = category(name="Java", num_of_courses="2", num_of_learners="168")
    
    Menu =  [
        menu(name="Browse Courses", categories = None),
        menu(name="Success Stories", categories = None),
        menu(name="About Us",categories = None)
]
    print("WELCOME TO AURIBISES")
    for idx in range(len(menu)):
        menu[idx].show()        
       
    
    
    

if __name__ == "__main__":
    main()