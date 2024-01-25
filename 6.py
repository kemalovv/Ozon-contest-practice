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