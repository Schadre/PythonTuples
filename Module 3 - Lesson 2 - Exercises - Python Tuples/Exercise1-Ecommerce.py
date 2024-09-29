def add_product(catalog):
    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        catalog.append((name, price, category))
    except ValueError:
        print("Invalid input, price must be a number")

def display_catalog(catalog):
    for product in catalog:
        print(f"Name: {product[0]}, Price: {product[1]}, Category: {product[2]}")

def search_category(catalog):
    category = input("Enter category to search: ")
    found = [product for product in catalog if product[2].lower() == category.lower()]
    if found:
        for product in found:
            print(f"Name: {product[0]}, Price: {product[1]}")
    else:
        print("No products found in this category.")

def main():
    catalog = []
    while True:
        print("\n1. Add a product")
        print("2. View catalog")
        print("3. Search by category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(catalog)
        elif choice == "2":
            display_catalog(catalog)
        elif choice == "3":
            search_category(catalog)
        elif choice == "4":
            print("Exiting program")
            break 
        else:
            print("Invalid choice, please try again")
if __name__ == "__main__":
    main()