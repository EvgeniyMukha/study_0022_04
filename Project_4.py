print("Первый овощ")
first = input()
print("Второй овощ")
second = input()
print("Третий овощ")
third = input()
Veg_1 = first.lower() # lower - ввод слов в нижнем регистре
Veg_2 = second.lower()
Veg_3 = third.lower()
print(Veg_1, Veg_2, Veg_3)
Veg_1 = first.upper() # upper - ввод слов в верхнем регистре
Veg_2 = second.upper()
Veg_3 = third.upper()
print(Veg_1, Veg_2, Veg_3)
Veg_1 = first.capitalize() # capitalize - выводит первую бувку в верхнем регистре
Veg_2 = second.capitalize()
Veg_3 = third.capitalize()
print(Veg_1, Veg_2, Veg_3)
print("Количество", Veg_1, "=")
first_num = int(input())
print("Количество", Veg_2, "=")
second_num = int(input())
print("Количество", Veg_3, "=")
third_num = int(input())
print("Всего: {0} - {1}; {2} - {3}; {4} - {5}.".format(Veg_1, first_num, Veg_2, second_num, Veg_3, third_num))
