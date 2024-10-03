""" 
Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement Sharpen your skills in
 managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where 
each book is stored as a tuple within a list. Your task is to 
update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding a
 duplicate book is handled appropriately.
"""
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def review_library(library):
    for item in library:
        print(f"Book Title: {item[0]}, Book Author: {item[1]}")


def update_library(library):
    book = input("Please enter the title: ")
    author = input("Please enter the author: ")
    new_book = (book, author)
    if new_book in library:
        print("This book already exist in our system.")
    else:
        library.append(new_book)
        print("Your new book as been added!")


def main():
    while True:
        print("\nWelcome to our Library Management System.")
        print("1. Enter a new book")
        print("2. Review Library")
        print("3. Quit")
        choice = input("Please select your option: ")

        if choice == "1":
            update_library(library)
        elif choice == "2":
            review_library(library)
        elif choice == "3":
            print("Have a nice day! Goodbye.")
            break
        else: 
            print("Error, please try again.")

if __name__ == "__main__":
    main()

