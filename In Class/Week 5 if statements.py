from tokenize import maybe


# answer = input('Should I do this? ')

# if answer == 'yes':
#     print('I did it!')
#     print('I did iti again')
#     print('and again')

# elif answer == "maybe": 
#     print("You need to make up your mind...")
#     #You can have as many elifs as you want but...
#     #they have to between the if and else in order to work
# else:
#     print("I didn't do it")

# print('done')

#The running-inator
go_running = 'You should go running, sorry'
dont_run = "DON'T DO IT!!!"
is_raining = input('Is it raining? ')

if is_raining.lower() == 'yes':
    print("DON'T DO IT!!!")
    
else:
    temp = float(input('What is the temp? '))
    if temp > 65:
        print(go_running)
    else:
        print(dont_run)