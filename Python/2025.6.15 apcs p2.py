from collections import Counter
m, n, k = map(int,input().split())#m = 輪盤數 , n = 輪盤中有幾個字 , k = 有幾回合 把以空格隔開的輸入分別存到m,n,k裡面
x, y = '',0
temp, score = 0,0
a, temp1st, zip_temp = [], [],''#暫存三個字串的串列以及暫存分數計算的變數

for i in range (m):
    temp1st.append(input())#先把輸入的三個字串輸入到一個串列中暫存

for l in range (k):
    a = list(map(int,input().split()))#回合數
    for j in range (m):
        x = temp1st[j]#取出字串做切片
        y = a[j]#依是哪個字串取出是哪個字串所對應的旋轉
        y %= n
        temp = x[-y::] + x[0:-y]
        temp1st[j] = temp
    for chars in zip(*temp1st):
        score += Counter(chars).most_common(1)[0][1]
print(score)