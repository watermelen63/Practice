#基本輸入
n, Sum, total_h, check = int(input()), 0, 0, []
global point
point = []
father = 0
point_val = {}

#找父節點
for i in range(n):
    Sum += (i + 1)

for i in range(n):
    arr = list(map(int, input().split()))
    point.append(arr)
    del arr[0]
    check.extend(arr)
    if point[i]:
        point_val.setdefault(f"{i + 1}", 1)
    else:
        point_val.setdefault(f"{i + 1}", 0)

#找H(T)
def find_height(father):
    global total_h
    global point_val
    ans = 0

    if not point[father - 1]:
        return 0
    
    max_h = 0
    for child in point[father - 1]:
        h = find_height(child)
        if h > max_h:
            max_h = h
            
    current_h = max_h + 1
    total_h += current_h
    return current_h

father = Sum - sum(check)
print(father)
find_height(father)
print(total_h)