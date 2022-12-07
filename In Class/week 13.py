def ask_yes_no(prompt, affirmative = 'y', negative = 'n'):
    response = ''
    # In Cases like this, While True is a valid option.
    while response != affirmative or response != negative:
        response = input(f'{prompt} ({affirmative.upper()}, {negative.upper()}) ').lower()
        if response == affirmative:
            return True
        if response == negative:
            return False
        else:
            print(f'Only "{affirmative}" or "{negative}" are valid options.')

is_raining = ask_yes_no('Is it raining? ')

if is_raining == True:
    print('Sorry you need to go running')