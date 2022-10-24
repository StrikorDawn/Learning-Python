from time import sleep
from turtle import delay
# Extra Credit! I showed and explained my game to 4 people!

cut_1 = 2
cut_2 = 3
awake = 4
option_cut = 1.5


print('Welcome to Project Varkalreon')
sleep(cut_1)
print('This is a halo inspired space text base adventure game! I hope you enjoy...')
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
        choice = 'pm'
        break
    elif planet.lower() == 'vantrogh 4' or planet.lower() == 'v4':
        landing = 'Vantrogh 4'
        choice = 'v4'
        break
    elif planet.lower() == 'montargen prime' or planet.lower() == 'mp':
        landing = 'Montargen Prime'
        choice = 'mp'
        break
    elif planet.lower() == 'zangariff' or planet.lower() == 'zg':
        landing = 'Zangariff'
        choice = 'zg'
        break
    else:
        print("I'm sorry... I don't quite understand what you mean.\n")

sleep(cut_1)
print(f'Understood. Setting course for {landing}.')

sleep(option_cut)

print(f'We will be landing shortly, best make your way to the hanger to gather you gear {name}…\n')

sleep(5)

while True:
    if choice == 'pm':
        print("Warning!")
        sleep(1)
        print("Warning!")
        sleep(1)
        print("Warning!")
        sleep(1)
        print(f"Guided landing systems off line, {name} report to the bridge and take the helm!")
        sleep(cut_2)
        print("Visibility is limited but there are 2 landing areas you can see the MOUNTAIN or the FLATS")
        land = input("Where would you like to land? ").lower()
        if land == 'mountain':
            print('''You safley land the craft on a flat patch in the mountains, you see a net work of tunnels
that lead deeper into the heart of the mountain, you also see
the rivers of lava pooling around the spires of the mountain.''')
            sleep(cut_1)
            print(f'''This planet is rich with Geothermal Activity. That could be a great energy source
the coloney would be able to utilize.''')
            choice2 = input("What would you like to do? STAY and explor the plannet and surrounding caves? or LEAVE and abandon this plannet? ").lower()
            if choice2 == 'stay':
                print(f'''You choose to stay and explore the mountain reaches of {landing}.
Your beacon is able to lead the colony to your location.
You are able to harnes the energy of this planet for the good of your people,
and keep you protected from the creatures that lurk on this shadowed plannet.''')
                break
            elif choice2 == 'leave':
                print(f'''After anylizing your surroundings despite it being rich with recorces,
and potential for renewable energy. You determined it not to be safe enought for the colony to reside here. 
You then leave the planet {landing} and set off accross the stars in search for a new home.''')
                break
                    
        elif land == 'flats':
            print(f''' You safley guide your ship to the flats of {landing}...
Apon landing you are met with an unexpected settling of the ship on the ground.
Systems indicate that the ship has sunken partialy into the ground!''')
            sleep(cut_1)
            print(f'''It does not appear that you will be able to launch from here.
On board you have enought rations to wait out the arrival of the colony.''')

            choice2 =input('Do you wish to STAY PUT? or EXPLORE the plannet? ').lower()
            if choice2 == 'stay put':
                print(f'''You decide to hunker down and anylize from the ship the activity on the planet.
You descover that this plannet is very volitile, and is filled with many large and dangerous creatures.
the ships defences keep you safe until and evacuation party is sent from the colony to take you home.
looks like the search goes on.''')
                break
                
            elif choice2 == 'explore':
                print(f'''You choose to get first hand experience of the plannet, it proves to be very dangerous.
All manor of large, strange creatures lerk in the shadows of this eclipsed plannet.
When the colony arrives they find nothing but a torn and empty ship,
scattered accorss the flats with no pilot to be found...''')
                break

    elif choice == 'v4':
        print(f'''Welcome to {landing}. The Terrain here seem very dusty and red. There seems to be some form of CITY off in the distance.
You are unsure whether any life forms may reside there. You also see a Large mountain with many CAVES, that could provide shelter and resources''').lower()
        sleep(cut_1)
        choice2 =input("What would you like to investigate? ")
        
        if choice2 == 'city':
            sleep(cut_1)
            print(f'''You approach the hive like city. It appears to be in partial ruin,
as if a battle long past raged through here.''')
            sleep(cut_1)
            stay = input("Would you like to STAY set up your base here? or EXPLORE else where on planet?").lower()
            
            if stay == "stay":
                sleep(cut_1)
                print(f'''You decide to stay and set up your base of operations in these city remains.
The local life on the plannet scouts you out from a distance but leaves you alone for the most part.
The fleet arives and you are succesfully able to establish a colony!''')
                break
            elif stay == 'explore':
                sleep(cut_1)
                print('''You choose to move on and explore the rest of the plannet.
In doing so, you get caught in a large wind storm and are lost to the elements''')
                break
        elif choice2 == 'caves':
            sleep(cut_1)
            print('''You choose to investigate the large cave systems.
You are greated by an inseclike species who dont seem to thrilled by your pressence.''')
            deeper= input('Would you like to go DEEPER? or return to the SHIP? ').lower()
            if deeper == 'deeper':
                sleep(cut_1)
                print('''The locals see you as hostile and begin to swarm you. 
Taking you prisoner and force you into slave labor, never to be seen again.''')
                break
            elif deeper == 'ship':
                sleep(cut_1)
                print('''Not wanting to risk an all out war with the locals,
you return back to you ship to re-evaluate potential locations.
Eventually you conclude that this planet is not fit for the Colony fly off back amogst the stars.''')
                break
    elif choice == 'mp':
        print(f'''Welcome to {landing}! ''')
        sleep(cut_1)
        print("Be advised this planet is heavlily vegitated, please report to the bridge for manual landing.")
        land=input(f'''When you arive at the bridge you are given two landing zones.
one in a forrested MEADOW and one on an open BEACH. Which do you choose? ''').lower()
        if land == 'meadow':
            sleep(cut_1)
            print(f'''As the ship lands your ears are greeted with the loud buzzing of a primal jungle.
You check your surrondings, and set up a perimiter to help fortify you position.''')
            sleep(cut_1)
            hide= input('''After a few days of little to no activity,
You hear the crashing of foliage mixed with heavy thudding of foot fall!
Do you INVESTIGATE or HIDE in the ship?''').lower()
            if hide == 'investigate':
                sleep(cut_1)
                print('''You go to investigate the sound of the desturbance, and some face to face with...
A T-REX! As you try to flee you are caught in it's gapping maw and swallowed whole!''')
                break
            elif hide == 'hide':
                sleep(cut_1)
                print('''You take refuge in your ship and see on your scanners...
Dosens of Prehistoric Life forms approaching you camp.
You make it out unharmed. But maybe this planet isn't the safest place to live after all...
At least not without the right tools!''')
                break
        if land == 'beach':
            sleep(cut_1)
            print('''You land on a large open beach, with a light breeze coming in with the tide.
As you look around more you see the bones of large fish scatterd beneath massive nests
resting in the tree tops!''')
            sleep(cut_1)
            print('''Looks like there might be some large type of bird that hunts these waters...
Best be warry of them.''')
            sleep(cut_1)
            hunt=input('''This area does look like it has a promising source of food!
Do you wish to explore the SEA, or hunt the BIRDS? ''').lower()
            if hunt == 'sea':
                sleep(cut_1)
                print('''You are able to find extreamly large fish in the water, some looking almost prehistoric!
You are able to remaine safe by keeping your wits about you.
You have found a good location for the Fleat to set up the colony!
Just be sure not to let down your Guard!''')
                break
            elif hunt == 'birds':
                sleep(cut_1)
                print('''You stake out the birds nest only to find that it belongs to a Pterodactyl!
What an amazing discovery, deffinetly don't want to become it's next meal tho!
As you continue to explore making sure to keep yourself out of hunting range of these dinosaurs,
you are able to find some plant life that will serve as a great source of food!
Congratulations! You have found a good place for the Colony!''')
                break
    elif choice == 'zg':
        print(f'''Welcome to {landing}!
You land on rocky mountain island, filled with tropical trees and sharp peaks.''')
        sleep(cut_1)
        food = input('''On the trees there are various tropical FRUITS, for you to inspect.
There are also large RIVER that rushes down the peaks of the mountain.
What would you like to inspect? ''').lower()
        if food == 'fruits':
            sleep(cut_1)
            print('''After inspecting the fruit, you have determied that it is safe to eat.
However, after a few days of eating the fruit, you develop an enduring case of the runs.
That is something that you should probably figure out how to deal with before the fleat arives.''')
            break
        elif food == 'river':
            sleep(cut_1)
            print('''The water is pure and clear, and seems safe to drink.
After gathering up materials and building a base of operations the fleat arrives.
You have succesfully compleated you mission! Congratulations!!!''')
            break