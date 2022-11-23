# file = open('data1.txt')

# for line in file:
#     print(line)

# file.close()
foods = []


with open('data1.txt') as file:
    for line in file:
        parts = line.split(',')
        for part in parts:
            foods.append(part.strip())
print(foods)
print('done')

with open('data2.txt') as file:
    header = file.readline()
    print(header)
    for line in file:
       parts = line.strip().split(',')
       food = parts[0]
       qty = int(parts[1])
       
       print(f'- {food} - {qty}')
print('done')