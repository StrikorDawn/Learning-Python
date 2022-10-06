from decimal import Rounded

child_price = float(input("What is the price of a child's meal? $"))
child_drink = float(input("What is the price fo a childs's Drink? $")) 
adult_price = float(input("What is the price of a adults's meal? $"))
adult_drink = float(input("What is the price fo a adults's Drink? $")) 
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax = float(input('What is the sales tax rate? 1.'))
print('---------------------------------')

subtotal = (child_price+child_drink)*children + (adult_price+adult_drink)*adults
sales_tax = (subtotal * tax)/100
total = round(subtotal+sales_tax, 2)
print(f'''
Subtotal: ${subtotal:.2f}
Sales Tax: ${sales_tax:.2f}
Total: ${total}
''')

payment = float(input(f'What is the payment amount? '))
change = payment - (subtotal+sales_tax)
print(f'Change: ${change:.2f}')
print('---------------------------------')
print(f'''
Thank You for dining with us!!!
      The Meat Shack inc.
''')