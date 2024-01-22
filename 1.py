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
