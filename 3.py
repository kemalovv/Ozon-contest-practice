# В Берляндии автомобильные номера состоят из цифр и прописных букв латинского алфавита. Они бывают двух видов:
# либо автомобильный номер имеет вид буква−цифра−цифра−буква−буква (примеры корректных номеров первого вида:
# R48FA, O00OO, A99OK); либо автомобильный номер имеет вид буква−цифра−буква−буква (примеры корректных номеров второго
# вида: T7RR, A9PQ, O0OO). Таким образом, каждый автомобильный номер является строкой либо первого, либо второго вида.
# Вам задана строка из цифр и прописных букв латинского алфавита. Можно ли разделить её пробелами на последовательность
# корректных автомобильных номеров? Иными словами, проверьте, что заданная строка может быть образована как
# последовательность корректных автомобильных номеров, которые записаны подряд без пробелов. В случае положительного
# ответа выведите любое такое разбиение.
# Пример теста 1:
# Входные данные:
# R48FAO00OOO0OOA99OKA99OK
# R48FAO00OOO0OOA99OKA99O
# A9PQ
# A9PQA
# A99AAA99AAA99AAA99AA
# AP9QA
# Выходные данные:
# R48FA O00OO O0OO A99OK A99OK
# -
# A9PQ
# -
# A99AA A99AA A99AA A99AA
# -


n = int(input())

while n > 0:
    number = input()
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    ans = []
    num = 0
    left = 0
    right = 0
    previous = 0

    for i in range(len(number)):
        if left > 1 or num > 2 or right > 2:
            ans = False
            break
        if left == 0 and number[i] in digits:
            ans = False
            break
        elif left == 0:
            left += 1
        elif left == 1 and not right and number[i] in digits:
            num += 1
        elif left == 1 and not num and number[i] not in digits:
            ans = False
            break
        elif num and number[i] not in digits:
            right += 1
            if right == 2:
                if i == len(number) - 1:
                    qty = previous + left + num + right
                    ans.append(number[previous:qty])
                    previous = qty
                    left, num, right = 0, 0, 0
                elif number[i + 1] not in digits:
                    qty = previous + left + num + right
                    ans.append(number[previous:qty])
                    previous = qty
                    left, num, right = 0, 0, 0
                else:
                    ans = False
                    break

    if not ans or previous != len(number):
        print("-")
    else:
        print(" ".join(ans))

    n -= 1