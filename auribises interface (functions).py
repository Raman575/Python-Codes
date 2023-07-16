from auribises import Course, Category, Menu
def main():
    Python_courses = [
        Course(name="Python for kids", price="3000", rating="4.5"),
        Course(name="Python with data science", price="12000", rating="4.9"),
        Course(name="Programming with Java SE", price="12000", rating="4.9"),
        Course(name="Full Stack Development", price="16000", rating="4.8")
    ]

    Typescript_courses = [
        Course(name="Typescript", price="10000", rating="4.5"),
       
    ]

    Java_courses = [
        Course(name="Java J2EE & SOA", price="16000", rating="4.9"),
        Course(name="App Development with Flutter", price="9000", rating="4.9")
    ]

    categories = [
        Category(name="Python", num_of_courses="4", num_of_learners="593", courses=Python_courses),
        Category(name="Typescript", num_of_courses="0", num_of_learners="0", courses=Typescript_courses),
        Category(name="Java", num_of_courses="2", num_of_learners="168", courses=Java_courses)
    ]

    menu = [
        Menu(name="Browse Courses", categories=categories),
        Menu(name="Success Stories", categories=None),
        Menu(name="About Us", categories=None)
    ]

    print("WELCOME TO AURIBISES")
    for menu_item in menu:
        menu_item.show()

    print()
    menu_option = int(input("Choose the menu (1-3): "))
    print("Choose Menu Option:", menu_option)

    if menu_option == 1:
        menu[0].show_categories()
        category_option = int(input("Choose the category (1-3): "))
        if category_option in range(1, len(categories) + 1):
            categories[category_option - 1].show_courses()
        else:
            print("Invalid category option.")

    elif menu_option == 2 or menu_option == 3:
        print("This menu option is currently unavailable.")
    else:
        print("Invalid menu option.")

if __name__ == "__main__":
    main()
    