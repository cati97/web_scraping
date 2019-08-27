from books_scraping.app import books

USER_CHOICE = """
-b -> look at 5-star books
-c -> to look at cheapest books
-n -> to just get the next available book
-q -> to exit

Your choice: """

books_gen = (b for b in books)  # generator for the books must be outside


def find_best_books():
    best_books = sorted(books, key=lambda x: (x.rating * - 1, x.price))
    for book in best_books:
        if book.rating == 5:
            print(book)


def find_cheapest_books(amount):
    cheapest_books = sorted(books, key=lambda x: x.price)[:int(amount)]
    for book in cheapest_books:
        print(book)


def get_next_book():
    print(next(books_gen))


user_choices = {
    'b': find_best_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'n'):
            user_choices[user_input]()
        elif user_input == 'c':
            amount = input("How many books do you want to see: ")
            find_cheapest_books(amount)
        else:
            print("I don't understand... Please try again")
        user_input = input('\nChoose again: ' + USER_CHOICE)
    else:
        print("Sorry to see you go. Bye")


menu()
