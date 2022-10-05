c_price = float(input("What is the price of a child's meal? "))
c_drink = float(input("What is the price fo a childs's Drink? ")) 
a_price = float(input("What is the price of a adults's meal? "))
a_drink = float(input("What is the price fo a adults's Drink? ")) 
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax = float(input('What is the sales tax rate? '))
print('---------------------------------')

subtotal = (c_price+c_drink)*children + (a_price+a_drink)*adults
sales_tax = (subtotal * tax)/100
print(f'''
Subtotal: ${subtotal}
Sales Tax: ${(subtotal * tax)/100}
Total: ${subtotal+sales_tax}
''')

payment = float(input(f'What is the payment amount? '))
change = payment - (subtotal+sales_tax)
print(f'Change: ${change}')
print('---------------------------------')