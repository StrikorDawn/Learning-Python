import random
word_list = ["reach",'space','cheese','goat','steak', 'banana','chief']
select = random.randint(0, len(word_list) - 1)
word = word_list[select]
play = True
secret = '_ '*len(word)
guess_count = 1

print(f"The word is: {secret}")

while play:
    guess = input("What is your guess? ")
    if len(guess) != len(word):
        print("Your guess must be the same length as the word.")
    elif guess != word:
        hint = ""
        for i, g_letter in enumerate(guess):
            is_in_word = False
            is_in_pos = False
            for j, s_letter in enumerate(word):
            
                if s_letter.lower() == g_letter.lower():
                    is_in_word = True
                    if i == j:

                        is_in_pos = True

            if is_in_word and is_in_pos:
                hint += g_letter.upper()
            elif is_in_word:
                hint += g_letter.lower()
            else:
                hint += "_"
            hint += " "
        print(f"Your hint is {hint}")
        guess_count = guess_count + 1
    else:
        print(f"Congradulations! You guessed correct in {guess_count}!")
        invalid = True
        while invalid:  
            again = input("Do you want to play again? ")
            if again.lower() == 'no':
                play = False
                invalid = False
            elif again.lower() == 'yes':
                play = True
                select = random.randint(0, len(word_list) - 1)
                word = word_list[select]
                secret = '_ '*len(word)
                guess_count = 1
                print(f"The word is: {secret}")
                invalid = False
            else:
                print('Invalid input must be yes or no.')