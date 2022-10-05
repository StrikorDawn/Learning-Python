num = 2.4
num2 = 2.1
#This does not work#
#print(int(num))

print (f'{num / num2:.2f}')
print (f'{num / num2:.2e}') #Scientific notation

amount = num/num2

# print(f'${num /num2:.2f}')

amount_rounded = round(amount, 3)

print(f'${amount:.2f} {amount_rounded}')

print('I'*23)

amount = float(input('how much was the sale? $'))
com_rate = float(input('how much is commission? '))
print(f'For a sale of ${amount:,.2f} the commission will be ${amount * com_rate:,.2f}')