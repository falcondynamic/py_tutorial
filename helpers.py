

def get_book_by_title(title, books):
    for book in books:
        if book["title"].lower() == title.lower():
            if book["availability"]:
                book["availability"] = False
                print(f"You have borrowed '{book['title']}'.")
            else:
                print(f"Sorry, '{book['title']}' is currently checked out.")
            break
        else:
            print(f"Book '{title}' not found in the library.")


def return_book_by_title(title, books):
    for book in books:
        if book["title"].lower() == title.lower():
            if not book["availability"]:
                book["availability"] = True
                print(f"You have returned '{book['title']}'.")
            else:
                print(f"Book '{title}' was not borrowed.")
            break
    else:
        print(f"Book '{title}' not found in the library.")