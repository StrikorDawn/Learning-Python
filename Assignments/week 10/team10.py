names = []
balances = []

print('Enter the names and baalances of bank accounts (type: quit when done)')
name = ''
biggest = 0

while name != 'quit':
    name = input('What is the name of the account? ').lower()
    if name != 'quit':
        balance = int(input('What is the Balance of the account? $'))
        names.append(name.title())
        balances.append(balance)

print("Account Information:")
for i in range(len(balances)):
    print(f'{i}. {names[i].title()}: ${balances[i]}')

for j, amount in enumerate(balances):
    if amount > biggest:
        biggest = amount
        spot = j


print(f'Total: {sum(balances)}')
print(f'Averages: {(sum(balances)/len(balances)):2f}')
print(f'Highest balance: {names[j]}: ${biggest}')

change = True
while change:
    update = input('Would you like to update an account? ').lower()

    if update == 'yes':
        account_number = int(input("What account index would you like to update? "))
        
        new_balance = int(input('What is the new amount? '))
        balances[account_number] = new_balance

    elif update == 'no':
        print("Account Information:")
        for i in range(len(balances)):
            print(f'{i}. {names[i].title()}: ${balances[i]}')
        change = False
    else:
        print('Must input yes or no.')


