from time import sleep
smallest = 99999999
largest = -1
select_smallest = 99999999
select_largest = 0

select_large_c = ''
select_small_c = ''
country = ''
# Year of interest
ages = []

option = input('Would you like to know about a specific COUNTRY or YEAR? ').lower()

if option == 'year':
    selection = int(input('Enter the year of interest: '))
elif option == 'country':
    selection = input('What country would you like to know about? ').lower()

with open('life-expectancy.csv') as file:
    file.readline()
    for data in file:
        stats = data.strip().split(',')
        countrys = stats[0]
        c_code = stats[1]
        year = int(stats[2])
        life_time = float(stats[3])
        
        if option == 'country':
            if countrys.lower() == selection:
                country = countrys
                ages.append(life_time)
                if life_time < smallest:
                    smallest = life_time

                if life_time > largest:
                    largest = life_time


        elif option == 'year':
            if life_time < smallest:
                smallest = life_time
                s_country = countrys

            if life_time > largest:
                largest = life_time
                l_country = countrys

            if year == selection:
                year_select = year
                ages.append(life_time)
                if life_time < select_smallest:
                    select_smallest = life_time
                    select_small_c = countrys

                if life_time > select_largest:
                    select_largest = life_time
                    select_large_c = countrys

    if option == 'year':      
        average = (sum(ages)/ len(ages))
        print(f'\nThe country of {s_country} has the overall lowest life expectancy, at {smallest} years. \nThe country of {l_country} has the overall largest at life expectancey at {largest} years.')

        print(f'\nFor the year {selection}')
        print(f'The average life expectancy across all countries was {average:.2f}')
        print(f'The max life expectancy was in {select_large_c} with {select_largest}')
        print(f'The min life expectancy was in {select_small_c} with {select_smallest}')
    
    elif option == 'country':
        average = (sum(ages)/ len(ages))
        print(f'The average life expectancy in {country} is {average:.2f}')
        print(f'The max life expectancy in {country} with {largest}')
        print(f'The min life expectancy in {country} with {smallest}')