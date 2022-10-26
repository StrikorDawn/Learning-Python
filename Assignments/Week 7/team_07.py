import random
play = 'yes'
while play == 'yes':

    number = random.randint(1,100)
    guess_cnt = 1
    u_guess = 0

    while u_guess != number:
        u_guess = int(input('What is the magic number? '))
        if u_guess > number:
            print('Lower')
            guess_cnt = guess_cnt + 1
        elif u_guess < number:
            print('Higher')
            guess_cnt = guess_cnt + 1
    print(f'Congrats! You guessed it in {guess_cnt} tries!')
    play = input('Would you like to play again? ').lower()
    if play == 'yes':
        play = 'yes'
    else:
        play = 'no'

print('Thanks for playing!')