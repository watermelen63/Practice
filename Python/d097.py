while True:
    try:
        temp = []
        ans = []
        count = []
        a = list(map(int, input().split()))
        L = a[0]
        del a[0]

        for i in range(L):
            if i != 0:
                temp.append(abs(a[i] - a[i - 1]))
        
        temp = sorted(temp)

        for j in range(L - 1):
            count.append(j + 1)

        if temp == count:
            print("Jolly")
        else:
            print("Not jolly")

    except EOFError:
        break