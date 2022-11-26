from time import sleep
countrys = []
c_codes = []
years = []
life_times = []

smallest = 99999999999
largest = -1

with open('life-expectancy.csv') as file:
    file.readline()
    for data in file:
        stats = data.strip().split(',')
        country = stats[0]
        c_code = stats[1]
        year = stats[2]
        life_time = float(stats[3])

        countrys.append(country)
        c_codes.append(c_code)
        years.append(year)
        life_times.append(life_time)

        if life_time < smallest:
            smallest = life_time

        if life_time > largest:
            largest = life_time

    print(f'\nThe lowest life expectancy in the data is {smallest} years, and the largest is {largest} years.')
