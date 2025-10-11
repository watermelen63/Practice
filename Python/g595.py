n = int(input())
List = list(map(int,input().split()))
temp = 0
for i in range (n):
    if List[i] == 0:
        if i == 0:
            temp += List[1]
        elif i == n-1:
            temp += List[-2]
        else:
            if List[i-1] > List[i+1]:
                temp += List[i+1]
            elif List[i+1] > List[i-1]:
                temp += List[i-1]
            elif List[i-1] == List[i+1]:
                temp += List[i+1]
print(temp)