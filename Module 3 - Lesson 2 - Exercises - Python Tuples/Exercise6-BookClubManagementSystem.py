def check_book(reading_list):
    title = input("Enter the title of the book to check: ")
    for book in reading_list:
        if book[0].lower() == title.lower():
            print(f"{title} has been read.")
            return 
    print(f"{title} has not been read.")

def total_books_read(reading_list):
    print(f"Total number if books read: {len(reading_list)}")

def find_first_by_author(reading_list):
    author = input("Enter the author's name: ")
    for i, book in enumerate(reading_list):
        if book[1].lower() == author.lower():
            print(f"The first book by {author} in the list is '{book[0]}'")
            return
    print(f"No books by {author} found in the reading list.")

def main():
    reading_list = (
        ("To Kill a Mockingbird", "Harper Lee"),
        ("1984", "George Orwell"),
        ("Pride and Prejudice", "Jane Austen")
    )

    while True:
        print("\n1. Check if a book has been read")
        print("2. View total number of books read")
        print("3. Find the first book by an author")
        print("4. Exit")
        choice = input("enter your choice: ")

        if choice == "1":
            check_book(reading_list)
        elif choice == "2":
            total_books_read(reading_list)
        elif choice == "3":
            find_first_by_author(reading_list)
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()