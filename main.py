from helpers import get_book_by_title, return_book_by_title
from database import get_file_books, get_sql_books, save_books_to_file, get_books_from_file

books = get_books_from_file()
commands = ("borrow <title>", "return <title>", "help", "exit", "list")

def main():
    while True:
        user_input = input("Enter book title (or exit): ")

        if user_input.lower() == "exit":
            save_books_to_file(books)
            break

        if user_input.lower() == "help":
            for command in commands:
                print(command)

        if user_input.strip() == "list":
            for book in books:
                status = "Available" if book["availability"] else "Checked out"
                print(f"{book['title']} - {status}")

        if user_input.startswith("borrow "):
            title = user_input[7:].strip()
            get_book_by_title(title=title, books=books)

        if user_input.startswith("return "):
            title = user_input[7:].strip()
            return_book_by_title(title=title, books=books)


if __name__ == "__main__":
    main()
