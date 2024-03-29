# Вы участвуете в разработке подсистемы проверки поля для игры <<Морской бой>>. Вам требуется написать проверку
# корректности количества кораблей на поле, учитывая их размеры. Напомним, что на поле должны быть: четыре
# однопалубных корабля, три двухпалубных корабля, два трёхпалубных корабля, один четырёхпалубный корабль.
# Вам заданы 10 целых чисел от 1 до 4. Проверьте, что заданные размеры соответствуют требованиям выше.
# Пример теста 1:
# Входные данные
# 5
# 2 1 3 1 2 3 1 1 4 2
# 1 1 1 2 2 2 3 3 3 4
# 1 1 1 1 2 2 2 3 3 4
# 4 3 3 2 2 2 1 1 1 1
# 4 4 4 4 4 4 4 4 4 4
# Выходные данные
# YES
# NO
# YES
# YES
# NO


n = int(input())

while n > 0:
    x = input()
    ships = [int(i) for i in x.split()]
    qty = {4: 1, 3: 2, 2: 3, 1: 4}
    ans = True

    for i in ships:
        qty[i] -= 1
        if qty[i] < 0:
            ans = False
            break

    if ans:
        print("Yes")
    else:
        print("No")
    n -= 1
