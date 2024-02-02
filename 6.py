# Реализуйте элемент функциональности простейшего терминала. Изначально терминал содержит одну пустую строку, в начале
# которой находится курсор.Ваша программа должна уметь обрабатывать последовательность символов (строку ввода).
# Обработка символа зависит от его значения: Строчная буква латинского алфавита или цифра обозначает, что
# соответствующий символ вставляется в положение курсора. Курсор сдвигается на позицию после вставленного символа. Буквы
# L и R обозначают нажатия стрелок влево и вправо. Они перемещают курсор на одну позицию влево или вправо. Если в
# соответствующем направлении нет символа, то операция игнорируется. Заметьте, что курсор в любом случае остаётся в той
# же строке. Буквы U и D обозначают нажатия стрелок вверх и вниз. Они перемещают курсор на одну позицию вверх или вниз.
# Если в соответствующем направлении нет строки, то операция игнорируется. Если строка есть, но в ней нужная позиция не
# существует, то курсор встаёт в конец строки. Буквы B и E обозначают нажатия клавиш Home и  End. Они перемещают курсор
# в начало или в конец текущей строки. Буква N обозначает нажатие клавиши Enter — происходит вставка новой строки. Если
# курсор находился не в конце текущей строки, то она разрывается, и часть после курсора переносится в новую строку.
# Курсор после этой операции стоит в начале новой строки.
# Пример теста 1:
# Входные данные:
# 4
# otLLLrRuEe256LLLN
# LRLUUDE
# itisatest
# abNcdLLLeUfNxNx
# Выходные данные:
# route
# 256
# -
#
# -
# itisatest
# -
# af
# x
# xb
# ecd
# -


n = int(input())

while n > 0:
    my_str = input()
    commands = ["L", "R", "U", "D", "B", "E", "N"]
    cur_index = 0
    cache = {0: []}
    rows = 0

    for i in range(len(my_str)):
        if my_str[i] not in commands:
            cache[rows].insert(cur_index, my_str[i])
            cur_index += 1
        elif my_str[i] == "L":
            if cur_index > 0:
                cur_index -= 1
        elif my_str[i] == "R":
            if cur_index < len(cache[rows]):
                cur_index += 1
        elif my_str[i] == "B":
            cur_index = 0
        elif my_str[i] == "E":
            cur_index = len(cache[rows])
        elif my_str[i] == "U":
            if rows:
                rows -= 1
                if cur_index > len(cache[rows]):
                    cur_index = len(cache[rows])
        elif my_str[i] == "D":
            if rows != len(cache) - 1:
                rows += 1
                if cur_index > len(cache[rows]):
                    cur_index = len(cache[rows])
        elif my_str[i] == "N":
            if rows != len(cache) - 1:
                for k in range(len(cache) - 1, rows, -1):
                    cache[k + 1] = cache[k]
                if cur_index == 0:
                    cache[rows + 1] = cache[rows]
                    cache[rows] = []
                    rows += 1
                    cur_index = 0
                elif cur_index == len(cache[rows]):
                    cache[rows + 1] = []
                    rows += 1
                    cur_index = 0
                else:
                    cache[rows + 1] = cache[rows][cur_index:]
                    cache[rows] = cache[rows][:cur_index]
                    rows += 1
                    cur_index = 0
            else:
                if cur_index == 0:
                    cache[rows + 1] = cache[rows]
                    cache[rows] = []
                    rows += 1
                    cur_index = 0
                elif cur_index == len(cache[rows]):
                    cache[rows + 1] = []
                    rows += 1
                    cur_index = 0
                else:
                    cache[rows + 1] = cache[rows][cur_index:]
                    cache[rows] = cache[rows][:cur_index]
                    rows += 1
                    cur_index = 0

    for i in range(len(cache)):
        if cache[i]:
            print("".join(cache[i]))
        else:
            print("")

    print("-")
    n -= 1