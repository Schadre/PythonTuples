def display_catalog(catalog):
    for book in catalog:
        print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

def search_by_title(catalog):
    title = input("Enter book title to search: ").lower()
    found = False
    for book in catalog:
        if book[0].lower() == title:
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
            found = True
            break
    if not found:
        print("Book not found")

def list_by_genre(catalog):
    genre = input("Enter genre to list books: ").lower()
    found = False 
    for book in catalog:
        if book[2].lower() == genre:
            print(f"Title: {book[0]}, Author: {book[1]}")
            found = True
    if not found:
        print("No books found in this genre.")

def main():
    catalog = (
        ("To Kill a Mockingbird", "Harper Lee", "Classic"),
        ("1984", "George Orwell", "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
        ("Brave New World", "Aldous Huxley", "Dystopian")
    )

    while True:
        print("\n1. View all books")
        print("2. Search by title")
        print("3. List by genre")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_catalog(catalog)
        elif choice == "2":
            search_by_title(catalog)
        elif choice == "3":
            list_by_genre(catalog)
        elif choice == "4":
            print("Exiting program")
            break 
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()