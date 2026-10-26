ans = {0:"普通", 1:"吉", 2:"大吉"}
m, d = map(int, input().split())
print(ans[(m * 2 + d) % 3])