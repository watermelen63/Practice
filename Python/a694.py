while True:
    try:
        n, m = map(int, input().split())
        food = [] #存 n * n 個食物的二維陣列最外圈

        for i in range(n): #輸入 n * n 的食物
            food.append(list(map(int, input().split())))

        for i in range(m): #輸入要吃哪個範圍
            Saturation = 0 #給某個看不懂英文的 飽食度
            x1, y1, x2, y2 = map(int, input().split())
            for j in range(x1 - 1, x2):
                for k in range(y1 - 1, y2):
                    Saturation += food[j][k]
            print(Saturation)


    except EOFError:
        break