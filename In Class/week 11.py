# file = open('data1.txt')

# for line in file:
#     print(line)

# file.close()
foods = []


with open('data1.txt') as file:
    for line in file:
        parts = line.split()
        for part in parts:
            foods.append(part)
print(foods)
print('done')