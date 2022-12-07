from cmath import pi
from time import sleep
run = True
def end():
    __quit= input('Would you like to continue? (yes/no) ').lower()
    while __quit != 'yes' or __quit != 'no':
        if __quit == 'yes':
            return True
        elif __quit == 'no':
            return False
        else:
            print('Please enter a valid option.\n')

while run:
    selection = input(f'What shape would you like to calculate (square, rectangle, circle)? ').lower()
        
    if selection == 'square':
        def area_of_sq_cm2():
            __square = float(input('What is the length of the side of the square in CM? '))
            __sq_cm2 = __square ** 2
            return __sq_cm2
        def area_of_sq_m2():
            __sq_m2 = sq_cm2/10000
            return __sq_m2

        sq_cm2 = area_of_sq_cm2()
        sq_m2 = area_of_sq_m2()
        print(f'The area of the square is {sq_cm2} cm^2 or {sq_m2} meters^2')
        run = end()

    elif selection == 'rectangle':
        def area_of_rectangle_cm2():
            __rl = float(input('What is the length of the rectangle in CM? '))
            __rw = float(input('What is the width of the rectangle in CM? '))
            __rec_cm2 = __rl*__rw
            return __rec_cm2

        def area_of_rectangle_m2():
            __rec_m2 = rec_cm2 / 10000
            return __rec_m2
        rec_cm2 = area_of_rectangle_cm2()
        rec_m2 = area_of_rectangle_m2()
        print(f'The area of the rectangle is {rec_cm2} cm^2 or {rec_m2} meters^2')
        run = end()

    elif selection == 'circle':

        def area_of_circle_cm2():
            circle = float(input('What is the radius of the circle in CM? '))
            __cir_cm2 = pi * circle**2
            return __cir_cm2
        def area_of_circle_m2():
            __cir_m2 = cir_cm2/ 10000 
            return __cir_m2

        cir_cm2 = area_of_circle_cm2()
        cir_m2 = area_of_circle_m2()
        print(f'The area of the circle is {cir_cm2} cm^2 or {cir_m2} meters^2')
        run = end()
    else:
        print('Please enter a valid selection.')
