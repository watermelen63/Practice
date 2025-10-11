temp=list(map(int,input('請以二十四小時制輸入時間[小時，分，秒](以空格分隔)\n').split()))
h,m,s=temp[0],temp[1],temp[2]
h1,m1,s1,h2=0,0,0,0
time=''
while True:
    if h < 0 or h > 23:
        print('error')
        break
    if m < 0 or m > 59:
        print('error')
        break
    if s < 0 or s > 59:
        print('error')
        break
    if h > 12:
        h2 = h - 12
        if h2 < 10:
            str(h2)
            h1=f"0{h2}"
        else:
            h1=str(h2)
        time = 'PM'
    else:
        h1=str(h)
        time = 'AM'
    if m < 10:
        m1=f"0{str(m)}"
    else:
        m1=str(m)
    if s < 10:
        s1=f"0{str(s)}"
    else:
        s1=str(s)
    print(h1 + ':' + m1 + ':' + s1,time)
    break