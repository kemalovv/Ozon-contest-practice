# Компрессия данных (англ. data compression) — алгоритмическое (обычно обратимое) преобразование данных,производимое
# с целью уменьшения занимаемого ими объёма. Вам предстоит реализовать простейший алгоритм компрессии последовательности
# чисел, который предполагает, что последовательность состоит из подряд идущих возрастающих или убывающих отрезков
# чисел. Формально, будем представлять результат компрессии как новую последовательность чётной длины вида b(1), c(1),
# b(2), c(2),..., b(k), c(k), где пара идущих подряд членов b(i), c(i) означает, что: если c(i) >= 0, что в искомой
# последовательности был возрастающий отрезок вида b(i), b(i) + 1, b(i) + 2,..., b(i) + c(i); если c(i) < 0, что в
# искомой последовательности был убывающий отрезок вида b(i), b(i) - 1, b(i) - 2,..., b(i) - c(i);
# По заданной последовательности a выведите такой результат сжатия, который имеет наименьшую длину
# (последовательность-результат содержит минимальное количество элементов). Если такое сжатие неоднозначно, то
# выведите любое из них.
# Пример теста 1:
# Входные данные:
# 5
# 9
# 3 2 1 0 -1 0 6 6 7
# 1
# 1000
# 7
# 1 2 3 4 5 6 7
# 7
# 1 3 5 7 9 11 13
# 11
# 100 101 102 103 19 20 21 22 42 41 40
# Выходные данные:
# 8
# 3 -4 0 0 6 0 6 1
# 2
# 1000 0
# 2
# 1 6
# 14
# 1 0 3 0 5 0 7 0 9 0 11 0 13 0
# 6
# 100 3 19 3 42 -2


qty = int(input())

for _ in range(qty):

    length = int(input())
    numbers = list(map(int, input().split()))
    increase = "check"
    diff = 0
    i = 0
    ans = []

    if length == 1:
        ans.append(numbers[0])
        ans.append(0)

    while i < length != 1:
        if increase == "check":
            if i == length - 1:
                ans.append(numbers[i])
                ans.append(0)
                break
            elif i == length - 2:
                if numbers[i] == numbers[i + 1] - 1 or numbers[i] == numbers[i + 1] + 1:
                    increase = numbers[i] < numbers[i + 1]
                    ans.append(numbers[i])
                    continue
                else:
                    ans.append(numbers[i])
                    ans.append(0)
                    ans.append(numbers[i + 1])
                    ans.append(0)
                    break

            elif numbers[i] == numbers[i + 1] - 1 or numbers[i] == numbers[i + 1] + 1:
                increase = numbers[i] < numbers[i + 1]
                ans.append(numbers[i])
                continue
            else:
                ans.append(numbers[i])
                ans.append(0)
                i += 1

        elif increase:
            if i == length - 1:
                break
            elif numbers[i] == numbers[i + 1] - 1:
                diff += 1
                i += 1
            else:
                ans.append(diff)
                diff = 0
                i += 1
                increase ="check"

        elif not increase:
            if i == length - 1:
                break
            elif numbers[i] == numbers[i + 1] + 1:
                diff -= 1
                i += 1
            else:
                ans.append(diff)
                diff = 0
                i += 1
                increase = "check"

    if diff:
        ans.append(diff)

    print(len(ans))
    print(" ".join(map(str, ans)))