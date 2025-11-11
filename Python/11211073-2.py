def searchChar(a, s):
    mid = len(a) // 2
    left = [:a]
    right = [a:]
    

ans, times = input(), int(input())
say, ans_temp = '', '*' * len(ans)
print(ans_temp)
for i in range(times):
    say = input()
    try:
        searchChar(ans, say)
    except say not in ans:
        print(ans_temp)