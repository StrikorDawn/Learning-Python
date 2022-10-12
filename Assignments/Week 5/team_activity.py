from codecs import getreader

grade = float(input('What is your grade percentage? '))
you_pass = 'Congradulations! You passed the class!'
fail = "Looks like you didn't quite make it, Come see me"
last_didget = grade % 10

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

if letter == 'A':
    n='n'
else:
    n=''

if last_didget >=7:
    sign = "+"
elif last_didget <= 3:
    sign = "-"
else:
    sign = ''

if grade >= 97:
    sign = ''
    
elif grade <= 59:
    sign = ''

if grade >=70:
    print(f"Congradulations! You got a{n} {sign}{letter}! You passed!")
else:
    print(f'''You got a {sign}{letter} in the class.
Keep at it and I know you'll do better next time!''')


