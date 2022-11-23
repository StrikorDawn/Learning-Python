with open('hr_system.txt') as file:
    for line in file:
        person = line.strip().split()
        name = person[0]
        id_number = person[1]
        title = person[2]
        salary = float(person[3])

        pay_check = salary / 24

        if title.lower() == 'engineer':
            pay_check += 1000

        print(f'{name} (ID: {id_number}), {title} - ${salary:.2f}')