from math_two import m

run = True
print(
    "/ - деление \n* - умножение \n+ - сложение \n- - разность\nm - модуль\narccos - arccos \n^ - возведение в степень \n! - факториал \nrand - рандомное число \nquit - выход")

while (run):
    str = input()

    if str == "/":
        m.de(self=(''))

    elif str == "quit":
        run = False

    elif str == "*":
        m.node(self=(''))

    elif str == "-":
        m.nosum(self=(''))

    elif str == "+":
        m.sum(self=(''))

    elif str == "^":
        m.s(self=(''))

    elif str == "m":
        m.mod(self=(''))

    elif str == "arccos":
        m.acos(self=(''))

    elif str == "!":
        print("numb =")
        numb = float(input())
        print(m.factorial(numb))

    elif str == "rand":
        m.r(self=(''))

    else:
        print("Такой нет команды")