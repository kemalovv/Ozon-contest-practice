t = int(input())

for _ in range(t):

    qty = int(input())
    my_list = input().split(",")
    done = []

    for i in my_list:
        if "-" in i:
            a, b = i.split("-")
            for j in range(int(a), int(b) + 1):
                if j not in done:
                    done.append(j)
        elif i not in done:
            done.append(int(i))
    streak = 0
    previous = 0
    ans = []

    for x in range(1, qty + 1):
        if streak:
            if x not in done:
                streak += 1
            elif streak == 1:
                ans.append(previous)
                streak = 0
                previous = 0
            else:
                ans.append(f"{previous}-{x - 1}")
                streak = 0
                previous = 0

        else:
            if x not in done:
                previous = x
                streak += 1

    if previous and streak > 1:
        ans.append(f"{previous}-{qty}")
    elif previous:
        ans.append(previous)

    print(",".join(map(str, ans)))

# 7
# 8
# 7
# 8
# 1,7,1
# 8
# 1-5,1,7-7
# 10
# 1-5
# 10
# 1,2,3,4,5,6,8,9,10
# 3
# 1-2
# 100
# 1-2,3-7,10-20,100