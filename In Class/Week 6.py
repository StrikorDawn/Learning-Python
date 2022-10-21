# and / or
# Boolean Types

# answer = input("Some Question? ").lower()

# if answer == 'yes' or answer== 'sure':
#     print('They said yes!')
# elif answer == 'no':
#     print('Maybe next time')
# else:
#     print('invalid option!')

#     or and not
    #they function as expected from Computer systems class.

from operator import truediv


go_running = 'You should go running, sorry'
dont_run = "DON'T DO IT!!!"
is_raining = input('Is it raining? ').lower() == 'yes'
temp = float(input('What is the temp? '))

if is_raining and temp > 78:
    should_run = True
elif is_raining:
    should_run = False
elif temp < 65:
    is_windy = input("Is it windy outside? ").lower() == 'yes'
    if is_windy and temp < 50:
        should_run = False
    else:
        should_run = True
else:
    should_run = True

if should_run:
    print(go_running)
else:
    print(dont_run)