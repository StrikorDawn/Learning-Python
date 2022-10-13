from time import sleep
from turtle import delay


cut_1 = 2
cut_2 = 3


print('Welcome to Project Varkalreon')
sleep(cut_1)
name = input('Before we begin... What is your name? ')

print('\nBeep...')
sleep(cut_1)
print('Beep...')
sleep(cut_1)
print('Beep...')
sleep(cut_1)
print('Vitals Stablizing...')
print('Cryogenic Hissing')
sleep(cut_1)
print('\nPod door opens\n')
sleep(cut_2)

if name.lower() == 'chief':
    print('Welcome Back Master Chief...')
elif name.lower() == 'master chief':
    print('Welcome Back Master Chief...')
else:
    print(f'Welcome Back Captain {name}...')
sleep(cut_1)

print(f'''\nYou have been in stasis for the past 23 years;
and we have arrived at the Varkalreon System right on Schedule...\n''')
sleep(cut_1)

print(f'''The rest of the fleet will be arriving soon.
Time is of the essince... 
You must complete your task, of finding a suitable planet for the colony before they arrive.\n''')
sleep(cut_1)

print(f'''There are a number of plannets in this sector that seem prospect...
Perkorda Major (PM)
Vantrogh 4 (V4)
Montargen Prime (MP)
Zangariff (ZG)
''')
