numbers =[]
run = 1
counter = 0
smallest = 999999999999999999
print('Enter a list of number, type 0 when finished.')
while run != 0:
    selection = int(input('Enter number: '))

    if selection != 0:
        numbers.append(selection)
        counter += 1
    if selection == 0:
        run = 0

average = sum(numbers)/counter
print(f'The sum is: {sum(numbers)}')
print(f'The average is: {average}')
print(f'The largest number is: {max(numbers)}')

for number in numbers:
    if number > 0 and number < smallest:
        smallest = number

print(f'The smallest positive number is: {smallest}')
print(f'The sorted list is: ')

sorted_list = sorted(numbers)

for i in sorted_list:
    print(i)