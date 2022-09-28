from cmath import pi
from time import sleep
delay = 1

square = float(input('What is the length of the side of the square in CM? '))
print(f'The area of the square is {square ** 2} cm^2 or {(square **2) / 10000} meters^2')
sleep(delay)

rl = float(input('What is the length of the rectangle in CM? '))
rw = float(input('What is the width of the rectangle in CM? '))
print(f'The area of the rectangle is {rl*rw} cm^2 or {(rl*rw) / 10000} meters^2')
sleep(delay)


circle = float(input('What is the radius of the circle in CM? '))
print(f'The area of the circle is {pi * circle**2} cm^2 or {(pi *circle**2) / 10000} meters^2')
sleep(delay)


lenght = float(input('What is the length? '))
print(f'''The area of the square is: {lenght ** 2}
The area of the square is: {pi * lenght**2}
The volume of the cube is: {lenght ** 3}
The voluem of a sphere is: {(4/3)* pi * lenght**3}''')