k,temp = int(input()),0
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
while k > 0:
    temp += k
    if temp % x1 == 0:
        k -= y1
    if temp % x2 == 0:
        k -= y2
print(temp)