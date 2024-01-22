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