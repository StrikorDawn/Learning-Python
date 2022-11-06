import random

word = 'reach'

hint = '_ '*len(word)

print(f'Here is a hint: {hint}')

guess = input('What is the word? ').lower()
guess_count = 1

while guess != word:
    print('Guess again')
    guess = input('What is the word? ').lower()
    guess_count = guess_count + 1

print(f"That's Correct! You got it in {guess_count} guesses!")