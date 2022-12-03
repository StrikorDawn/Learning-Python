from time import sleep
largest = 0
book = ''
volumes = [
    'Old Testament',
    'New Testament',
    'Book of Mormon',
    'Doctrine and Covenants',
    'Pearl of Great Price'
]
print('Here are the different Volumes of Scripture.')
for i in volumes:
    print(f' - {i}')
    sleep(.5)
    
selection =input('Which volume of scripture would you like to know about? ').lower()

with open('books_and_chapters.txt') as file:
    for line in file:
        data = line.strip().split(':')
        books = data[0]
        chapter = int(data[1])
        scripture = data[2]

        if scripture.lower() == selection:
            print(f'\nScripture: {scripture}, Book: {books}, Chapters: {chapter}')
            if largest < chapter:
                largest = chapter
                book = books

print(f'\nIn the {selection.title()}, The book of {book} has largest number of chapters, for a total of {largest}!')