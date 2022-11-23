with open('books.txt') as file:
    for books in file:
        print(books.strip())