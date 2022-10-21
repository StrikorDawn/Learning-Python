from time import sleep
from turtle import delay


cut_1 = 2
cut_2 = 3
awake = 4
option_cut = 1.5


print('Welcome to Project Varkalreon')
sleep(cut_1)
print('This is a halo inspired space text base adventure game! I hope you enjoy...')
sleep(cut_1)
name = input('Before we begin... What is your name? ')

# print('\nBeep...')
# sleep(cut_1)
# print('Beep...')
# sleep(cut_1)
# print('Beep...')
# sleep(cut_1)
# print('Vitals Stablizing...')
# print('Cryogenic Hissing')
# sleep(cut_1)
# print('\nPod door opens\n')
# sleep(cut_2)

if name.lower() == 'chief' or name.lower() == 'master chief':
    name = "Master Chief"
    print(f'Welcome Back {name}...')
else:
    print(f'Welcome Back Captain {name}...')
    captain = f'Captain {name}'
    name = captain

sleep(cut_1)

print(f'''\nYou have been in stasis for the past 23 years;
and we have arrived at the Varkalreon System right on Schedule...\n''')
sleep(awake)

print(f'''The rest of the fleet will be arriving soon.
Time is of the essince... 
You must complete your task, of finding a suitable planet for the colony before they arrive.\n''')
sleep(awake)

print('There are a number of plannets in this sector that seem prospect...')
sleep(option_cut)
print('   (PM) Perkorda Major')
sleep(option_cut)
print('   (V4) Vantrogh 4')
sleep(option_cut)
print('   (MP) Montargen Prime')
sleep(option_cut)
print('   (ZG) Zangariff \n')
sleep(cut_1)

while True:

    planet = input('Which planet would you like to investigate? ')
    if planet.lower() == 'perkorda major' or planet.lower() =='pm':
        landing = 'Perkorda Major'
        break
    elif planet.lower() == 'vantrogh 4' or planet.lower() == 'v4':
        landing = 'Vantrogh 4'
        break
    elif planet.lower() == 'montargen prime' or planet.lower() == 'mp':
        landing = 'Montargen Prime'
        break
    elif planet.lower() == 'zangariff' or planet.lower() == 'zg':
        landing = 'Zangariff'
        break
    else:
        print("I'm sorry... I don't quite understand what you mean.\n")

sleep(cut_1)
print(f'Understood. Setting course for {landing}.')

sleep(option_cut)

print(f'We will be landing shortly, best make your way to the hanger to gather you gear {name}…\n')
