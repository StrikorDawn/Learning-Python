import time

print('hello world', end= '\r')
time.sleep(3)
print('hello there')


str = 'hello world'

for letter in str:
    print(letter, end='')
    time.sleep(1)