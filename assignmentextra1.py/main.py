# Library Management CLI

library = []  # List to store book dictionaries


def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    try:
        year = int(input("Enter year of publication: "))
    except ValueError:
        print("Year must be a number. Book not added.")
        return
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }
    library.append(book)
    print(f"Book '{title}' added successfully!\n")


def list_books():
    if not library:
        print("No books in the library.\n")
        return
    print("Books in the library:")
    for idx, book in enumerate(library, 1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {status}")
    print()


def search_books():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {status}")
            found = True
    if not found:
        print("No matching books found.\n")
    print()


def borrow_book():
    title = input("Enter the title of the book to borrow: ").lower()
    for book in library:
        if book["title"].lower() == title:
            if book["available"]:
                book["available"] = False
                print(f"You have borrowed '{book['title']}'.\n")
            else:
                print(f"'{book['title']}' is currently unavailable.\n")
            return
    print("Book not found.\n")


def return_book():
    title = input("Enter the title of the book to return: ").lower()
    for book in library:
        if book["title"].lower() == title:
            if not book["available"]:
                book["available"] = True
                print(f"You have returned '{book['title']}'.\n")
            else:
                print(f"'{book['title']}' was not borrowed.\n")
            return
    print("Book not found.\n")


def main():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("Exiting the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
