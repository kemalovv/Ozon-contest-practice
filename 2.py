n = int(input())

while n > 0:
    day, month, year = map(int, input().split())
    months2 = [4, 6, 9, 11]

    leap_year = True if not year % 400 or (not year % 4 and year % 100) else False

    ans = True

    if month in months2 and day > 30:
        ans = False
    elif month == 2:
        if leap_year:
            if day > 29:
                ans = False
        elif day > 28 and not leap_year:
            ans = False

    if ans:
        print("Yes")
    else:
        print("No")
    n -= 1