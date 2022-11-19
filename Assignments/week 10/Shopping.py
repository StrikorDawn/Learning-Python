from time import sleep
#Taden Marston

selection = 0

menu = [
    '1. Add item',
    '2. View cart',
    '3. Remove item',
    '4. Compute total',
    '5. Quit',
]
in_cart = []
cart_cost = []

print('Welcome to the Shopping Cart Program!')
sleep(0.5)
while selection != 5:
    
    print("\nPlease select one of the following #'s: ")
    for option in menu:
        print(f'  {option}')
        sleep(0.5)
    selection = int(input('Please enter an action: '))
    if selection == 1:
        add_cart = input(f"\nWhat would you like to to add? ").lower()
        in_cart.append(add_cart)
        item_cost = float(input(f"What is the cost of {add_cart.title()}? $"))
        cart_cost.append(item_cost)

        print(f"\n'{add_cart.title()}' has been added to the cart.")
        
    if selection == 2:
        print(f'\nThe contents of the shoppingcart are: ')
        for i in range(len(in_cart)):
            print(f'{i+1}. {in_cart[i].title()} - ${cart_cost[i]}')
            sleep(0.5)

    if selection == 3:
        print(f'\nThe contents of the shoppingcart are: ')
        for i in range(len(in_cart)):
            print(f'{i+1}. {in_cart[i].title()} - ${cart_cost[i]}')
            sleep(0.5)
        remove = int(input(f'\nWhat item # would you like to remove? '))
        print(f'\n{in_cart[remove - 1].title()} has been removed.')
        in_cart.pop((remove - 1))
        cart_cost.pop((remove - 1))

            
    if selection == 4:
        total = sum(cart_cost)
        print(f"\nThe Total cost of your cart is ${total}.")


print("\nThank you for shopping with us. Have a fantastic day!")