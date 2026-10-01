data = int(input())
distance = 0

for _ in range(data):
    temp = list(map(int, input().split()))
    tmp = temp[0]#暫存有多少門牌號碼的量
    del temp[0]
    temp = sorted(temp)

    if len(temp) % 2 != 0:
        c = tmp // 2
        home = temp[c]
    else:
        c = tmp // 2 - 1#找中間
        a = temp[c]
        b = temp[c + 1]
        home = (a + b) / 2

    count = 0
    for i in temp:
        count += abs(home - i)
    print(int(count))