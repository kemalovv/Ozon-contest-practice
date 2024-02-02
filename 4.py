# В офисе стоит кондиционер, на котором можно установить температуру от 15 до 30 градусов. В офис по очереди приходит n
# сотрудников. i-ый из них желает температуру не больше или не меньше a(i). После прихода каждого сотрудника
# определите, можно ли выставить температуру, которая удовлетворит всех в офисе.
# Пример теста 1:
# Входные данные:
# 4
# 1
# >= 30
# 6
# >= 18
# <= 23
# >= 20
# <= 27
# <= 21
# >= 28
# 3
# <= 25
# >= 20
# >= 25
# 3
# <= 15
# >= 30
# <= 24
# Выходные данные:
# 30
#
# 18
# 18
# 20
# 20
# 20
# -1
#
# 15
# 20
# 25
#
# 15
# -1
# -1


n = int(input())

while n > 0:
    s = int(input())
    temperature = [15, 30]
    while s > 0:
        temp = input().split()
        temp[1] = int(temp[1])

        if temp[0] == ">=" and temperature[0] < temp[1]:
            temperature[0] = temp[1]
        elif temp[0] == "<=" and temperature[1] > temp[1]:
            temperature[1] = temp[1]
        elif temp[0] == ">=" and temp[1] > 30:
            print("-1")
            s -= 1
            for i in range(s):
                input()
                print("-1")
            break
        elif temp[0] == "<=" and temp[1] < 15:
            print("-1")
            s -= 1
            for i in range(s):
                input()
                print("-1")
            break

        if temperature[0] > temperature[1]:
            print("-1")
            s -= 1
            for i in range(s):
                input()
                print("-1")
            break
        else:
            print(temperature[0])
            s -= 1

    print("")
    n -= 1