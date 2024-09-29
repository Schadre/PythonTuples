def display_menu(menu):
    print("\nComplete Menu:")
    for item in menu:
        print(f"- {item}")

def display_section(section, section_name):
    print(f"\n{section_name}")
    for item in section:
        print(f"- {item}")


def main():
    starters = ("Bruschetta", "Caesar Salad", "Tomato Soup")
    main_courses = ("Spaghetti Carbonara", "Margherita Pizza", "Grilled Salmon")
    desserts = ("Tiramisu", "Panna Cotta", "Gelato")

    full_menu = starters + main_courses + desserts

    while True:
        print("\n1. View entire menu")
        print("2. View starters")
        print("3. View main courses")
        print("4. View desserts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu(full_menu)
        elif choice == "2":
            display_section(starters, "Starters")
        elif choice == "3":
            display_section(main_courses, "Main Courses")
        elif choice == "4":
            display_section(desserts, "Desserts")
        elif choice == "5":
            print("Exiting program.")
            break 
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()