import json
import faker
from .contants import EXIT_COMMAND

print(f"Constant from contants.py: {EXIT_COMMAND}")

fake = faker.Faker()

def get_books_from_file():
    books = []
    try:
        with open("database/file/books.txt", "r") as file:
            books_json = file.read()
            books = json.loads(books_json)
    except FileNotFoundError:
        pass
    return books

def save_books_to_file(books):
    try:
        with open("books.txt", "w") as file:
            books_json = json.dumps(books)
            file.write(books_json)
    except Exception as e:
        print(f"Error saving books to file: {e}")

def get_books():
    return [{"id": 1, "title": "File", "availability": True}]