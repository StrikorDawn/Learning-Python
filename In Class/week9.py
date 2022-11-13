from time import sleep
# variable = []

# movies = [
#     'Batman', 
#     'Princess Bride',
#     'Avengers'
#     ]

# movies.append('Black Panther')

# #print(movies)
# print('Movies:')
# for movie in movies:
#     print(f'\t- {movie}')

print()
menu = [
    '1- Drink',
    '2- Entree',
    '3- Side',
]
selections = []

menu.append('4- Desert')
menu.append('5- Order Complete')
drinks = ['Water', 'Dr. Pepper', 'Sprite', 'Root Beer', 'Mountain Dew']
entrees = ['Burger', 'Mac n Cheese', 'Chicken Nuggets', 'Chicken Sandwitch', 'Pizza']
sides = ['Fries', 'Mashed Potatos', 'Salad', 'Bread Sticks', 'Rolls']
deserts = ['Ice Cream', 'Pie', 'Cinnomon Roll',]

selection = 0
print('Welcome to my resturant!\n')
sleep(0.5)
while selection != 5:
    print('Menu: ')
    for item in menu:
        print(f' - {item}')
        sleep(0.5)
    selection = int(input('What would you like? '))
    print()
    if selection >= 6 or selection <= 0:
        print('Input must be between 1-5')
    else:
        if selection == 1:
            print('Drink options are: ')
            for drink in drinks:
                print(f' {drink.title()}')
                sleep(0.5)
            user_drink = input('What would you like to drink? ').title()
            selections.append(user_drink)
        elif selection == 2:
            print('Entree options are: ')
            for entree in entrees:
                print(f' {entree.title()}')
                sleep(0.5)
            user_entree = input('What entree would you like? ').title()
            selections.append(user_entree)
        elif selection == 3:
            print('Side options are: ')
            for side in sides:
                print(f' {side.title()}')
                sleep(0.5)
            user_side = input('What side would you like? ').title()
            selections.append(user_side)
        elif selection == 4:
            print('Desert options are: ')
            for desert in deserts:
                print(f' {desert.title()}')
                sleep(0.5)
            user_desert = input('What desert would you like? ').title()
            selections.append(user_desert)

print()
print(f'You selected: {selections}')