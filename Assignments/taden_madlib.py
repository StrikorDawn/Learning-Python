from time import sleep
delay = 1.5
delay2 = 1
print('Welcome to Madlib Reading "Big Trouble"')
sleep(delay)
print('Please provide a word for each of the catagories presented...')
sleep(delay)
adj = input('adjective: ')
animal = input('animal: ')
v1= input('verb: ')
exclame = input('exclamation: ') 
v2= input('verb: ')
v3= input('verb: ')
exclame2= input('exclamation:')
v4= input('verb: ')
adverb= input('adverb: ')
song= input('song line: ')

sleep(delay2)
print(f'''The other day, I was really in trouble. It all started when I saw a very
{adj} {animal} {v1} down the hallway. "{exclame}!" I yelled. But all
I could think to do was to {v2} over and over. Miraculously,
that caused it to stop, but not before it tried to {v3}
right in front of my family. "{exclame2}" I shouted, 
as my family began to {v4}! As the {animal} {adverb} along after them.
All the while the {animal} was singing...
"{song}"''')
