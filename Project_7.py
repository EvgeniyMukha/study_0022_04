def writing_file(name):
    mass = []

    r = 0

    file = open(name + ".txt", "r")

    # заполняем массив строками
    for line in file:
        mass.append(line)
    file.close
    file = open(name + ".txt", "w")

    for key, val in dictionary.items():
        file.write('{}:{}\n'.format(key, val))
    file.close
    file = open(name + ".txt", "a")

    for i in range(len(mass)):
        file.write(mass[i])
    file.close


list_1 = []
list_2 = []

print("Для выхода из цикла введите - quit")

while (True):
    c = input()
    if c == "quit":
        break
    else:
        list_1.append(c)

set_2 = set(list_1)
print("список -", list_1)
print("множество - ", set_2)
print("количество символов в cgbcrt =", len(list_1))
print("заполните следующий список из", len(list_1), "символов")

for i in range(len(list_1)):
    c = input()
    list_2.append(c)

print(list_2)
complex = {list_2[i]: list_1[i] for i in range(len(list_1))}

print("Введите название файла")
name = input()

dictionary = complex

try:
    writing_file(name)
except IOError as e:
    file = open(name + ".txt", "a")
    writing_file(name)