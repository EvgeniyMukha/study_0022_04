list_1 = []
list_2 = []


def completion_mass_keys():
    str = []
    while (True):
        c = input()
        if c == "quit":
            break
        else:
            str.append(c)
    return str


def completion_mass_values(str):
    str_3 = []
    for i in range(len(str)):
        check = input()
        str_3.append(check)
    return str_3


def completion_lists(str_3, str):
    summ = {str[i]: str_3[i] for i in range(len(str))}
    return summ


print("Для выхода из цикла введите - quit")
list_1 = completion_mass_keys()

mass_2 = set(list_1)
print("список -", list_1)
print("множество - ", mass_2)
print("количество символов в списке =", len(list_1))
print("заполните следующий список из", len(list_1), "символов")

list_2 = completion_mass_values(list_1)

print(list_2)
list = completion_lists(list_2, list_1)
print(list)