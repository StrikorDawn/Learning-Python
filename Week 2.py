from unicodedata import name
# name ='bob'
# last_name = 'Jeffery'

# full_name= f'Your Nmae is: {name} {last_name}'

# print(name)
# print('your name is: ' + name) 
# print('Your name is: {} {}'.format(name, last_name))
# # # 0 = first "argument/variable" and 1 = second argument and so on...
# print('Your name is: {1} {0}'.format(name, last_name)) 

# ### Python 3 only

# print(f'Your name is: {name} {last_name}')

# #Other methods for manipulation of text

# print(full_name)

# print(name.capitalize()) #will captilize the first letter in the string.
# print(name.upper()) #makes everything upper case
# print(name.lower()) #makes everything lower case
# print(name.title()) #does first letter of all words

# #Data Collection
# print(f'Your name is: {name} {last_name}'.upper().count('O'))

print('''Dear Student
We are pleased to announce...''')

#or
print('''Dear Student\n
We are pleased to announce''')

name = 'Taden'
course = 'CSE 110'
day = 'Monday'
date = '12'
month = 'October'

print(f'''Dear {name}
We are pleased to announce you rclass {course} will begin on
{day} the {date} of {month}''')