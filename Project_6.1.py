list_1 = []
list_2 = []


def mass_keys():
    str = []
    while (True):
        word = input()
        if word == "quit":
            break
        else:
            str.append(c)
    return str


def mass_values(str):
    str_3 = []
    for i in range(len(str)):
        word = input()
        str_3.append(word)
    return str_3


def multipl(str_3, str):
    summ = {str[i]: str_3[i] for i in range(len(str))}
    return summ


print("Для выхода из цикла введите - quit")
list_1 = mass_keys()

multiplicity = set(list_1)
print("список -", list_1)
print("множество - ", multiplicity)
print("количество символов в списке =", len(list_1))
print("заполните следующий список из", len(list_1), "символов")

list_2 = mass_values(list_1)

print(list_2)
list = multipl(list_2, list_1)
print(list)
