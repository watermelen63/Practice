def region(x1, y1, x2, y2):#計算方形面積的函數
    return abs((x1 - x2) * (y1 - y2))

total_region = 100 * 100
N = int(input()) #夜晚數
guard_1, guard_2 = [], []
strongly_region, weakly_region, unsecured_region = 0, 0, 0

for i in range (N):
    guard_1 = list(map(int, input().split()))
    guard_2 = list(map(int, input().split()))
    strongly_region = region(guard_1[2], guard_1[3], guard_2[0], guard_2[1])
    weakly_region = (region(guard_1[2], guard_1[3], guard_1[0], guard_1[1])
    + region(guard_2[2], guard_2[3], guard_2[0], guard_2[1]) - strongly_region * 2)
    unsecured_region = total_region - weakly_region - strongly_region

    print(f"Night {i + 1}: {strongly_region} {weakly_region} {unsecured_region}")