import time
my_list = ['cheese', 'bread', 'mayo', 'mustard']

for i in range(101):
    print ('\r'+str(i)+'% completed',)
    time.sleep(0.1)