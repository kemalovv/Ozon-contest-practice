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