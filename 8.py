# Колода состоит из 52 карт. Каждая карта обозначается одним из тринадцати значений ("2", "3", "4", "5", "6", "7", "8",
# "9", "T", "J", "Q", "K", "A") и одной из четырех мастей ("S", "C", "D", "H"). Выдуманная игра 3-Покер происходит
# следующим образом.
# 1. Изначально все n игроков получают по две карты из колоды.
# 2. После этого на стол выкладывается одна карта из той же колоды.
# 3. Выигрывают те игроки, у которых собралась самая старшая комбинация.
# Для определения самой старшей комбинации, которая собралась у i-го игрока, используются следующие правила:
# Если две карты у игрока в руке и карта на столе имеют одинаковое значение, игрок собрал комбинацию ‘Сет со значением
# x’; если из двух карт у игрока в руке и карты на столе можно выбрать две карты с одинаковым значением x, игрок собрал
# комбинацию ‘Пара со значением x’; иначе, берется карта с самым старшим значением из двух карт у игрока в руке и карты
# на столе, тогда игрок собрал комбинацию ‘Старшая карта x’.
# Любой сет старше пары, а любая пара старше комбинации старшая карта. Из одинаковых комбинаций старше та, у которой
# старше значение. Если одинаковая самая старшая комбинация есть у нескольких игроков, все они объявляются выигрывшими.
# Вы — первый игрок. Вам известно, какие карты получил на руки каждый игрок. Определите, какую карту можно выложить на
# стол, чтобы вы оказались в числе победителей.
# Пример теста 1:
# Входные данные:
# 4
# 2
# TS TC
# AD AH
# 3
# 2H 3H
# 9S 9C
# 4D QS
# 3
# 4C 7H
# 4H 4D
# 6S 6H
# 3
# 2S 3H
# 2C 2D
# 3C 3D
# Выходные данные:
# 2
# TD
# TH
# 0
# 3
# 7S
# 7C
# 7D
# 0


t = int(input())

for _ in range(t):
    players_qty = int(input())
    my_cards = input().split()
    cards = [(input().split()) for _ in range(players_qty - 1)]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    values_qty = {"2": ["S", "C", "D", "H"],
                  "3": ["S", "C", "D", "H"],
                  "4": ["S", "C", "D", "H"],
                  "5": ["S", "C", "D", "H"],
                  "6": ["S", "C", "D", "H"],
                  "7": ["S", "C", "D", "H"],
                  "8": ["S", "C", "D", "H"],
                  "9": ["S", "C", "D", "H"],
                  "T": ["S", "C", "D", "H"],
                  "J": ["S", "C", "D", "H"],
                  "Q": ["S", "C", "D", "H"],
                  "K": ["S", "C", "D", "H"],
                  "A": ["S", "C", "D", "H"]
                  }
    my_pair = 0

    if my_cards[0][0] == my_cards[1][0]:
        my_pair = 1
        values_qty[my_cards[0][0]].remove(my_cards[0][1])
        values_qty[my_cards[1][0]].remove(my_cards[1][1])
    else:
        values_qty[my_cards[0][0]].remove(my_cards[0][1])
        values_qty[my_cards[1][0]].remove(my_cards[1][1])

    is_pair = []

    for i in cards:
        if i[0][0] == i[1][0]:
            is_pair.append(1)
            values_qty[i[0][0]].remove(i[0][1])
            values_qty[i[1][0]].remove(i[1][1])

        else:
            is_pair.append(0)
            values_qty[i[0][0]].remove(i[0][1])
            values_qty[i[1][0]].remove(i[1][1])

    ans = []

    for k, v in values_qty.items():
        is_valid = True

        if my_pair and k == my_cards[0][0]:
            pass

        elif my_pair:
            for i in range(len(cards)):
                if is_pair[i] and cards[i][0][0] == k:
                    is_valid = False
                    break
                elif is_pair[i] and values.index(cards[i][0][0]) > values.index(my_cards[0][0]):
                    is_valid = False
                    break
                elif not is_pair[i] and cards[i][0][0] == k and values.index(cards[i][0][0]) > values.index(
                        my_cards[0][0]):
                    is_valid = False
                    break
                elif not is_pair[i] and cards[i][1][0] == k and values.index(cards[i][1][0]) > values.index(
                        my_cards[0][0]):
                    is_valid = False
                    break

        elif not my_pair and my_cards[0][0] == k:
            for i in range(len(cards)):
                if is_pair[i] and cards[i][0][0] == k:
                    is_valid = False
                    break
                elif is_pair[i] and values.index(cards[i][0][0]) > values.index(my_cards[0][0]):
                    is_valid = False
                    break

        elif not my_pair and my_cards[1][0] == k:
            for i in range(len(cards)):
                if is_pair[i] and cards[i][0][0] == k:
                    is_valid = False
                    break
                elif is_pair[i] and values.index(cards[i][0][0]) > values.index(my_cards[1][0]):
                    is_valid = False
                    break

        elif not my_pair:
            for i in range(len(cards)):
                if is_pair[i]:
                    is_valid = False
                    break
                elif not is_pair[i] and (cards[i][0][0] == k or cards[i][1][0] == k):
                    is_valid = False
                    break
                elif not is_pair[i] and max(values.index(cards[i][0][0]), values.index(cards[i][1][0]),
                                            values.index(k)) > max(values.index(my_cards[0][0]),
                                                                   values.index(my_cards[1][0]), values.index(k)):
                    is_valid = False
                    break

        if is_valid:
            for x in v:
                ans.append(f"{k}{x}")

    print(len(ans))
    for result in ans:
        print(result)



