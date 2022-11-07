word = 'commitment'
length = len(word)

letter = input('What is your favorite letter? ').lower()

for i in word:
    if letter == i:
        i = "_"
    
    print(i,end="")

print()
first_name = 'Brigham'

for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")

yes = True

while yes:

    quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

    num = int(input("Please enter a number: " ))

    for i, letter in enumerate(quote):
        if i % num == 0:
            letter = letter.upper()
        print(letter,end="")
    print()
    try_again = input('Would you like try again?(Yes/No) ')
    if try_again != yes:
        yes = False