word = "reach"
play = True
secret = '_ '*len(word)
guess_count = 1

print(f"The word is: {secret}")
while play:
    guess = input("What is your guess? ")

    for i in enumerate(word):
        for a, g_letter in enumerate(guess):
            if guess != word:
                print('Guess again')
                print(f"Your hint is: {secret}")
                guess = input('What is the word? ').lower()
                guess_count = guess_count + 1
            else:
                print("Guess must be same length as word.")

print(f"That's Correct! You got it in {guess_count} guesses!")