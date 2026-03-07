n, Sum, point, check = int(input()), 0, [], []
father = 0

for i in range(n):
    Sum += (i + 1)

for i in range(n):
    arr = list(map(int, input().split()))
    point.append(arr)
    del arr[0]
    check.extend(arr)

father = Sum - sum(set(check))
print(father)