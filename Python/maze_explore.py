# 將輸入轉成迭代器，方便一個一個取出
data = iter(map(int, input().split()))
total_diff = 0

def solve(parent_id):
    global total_diff
    try:
        current_id = next(data) # 取出下一個數字
    except StopIteration:
        return

    if current_id == 0: # 碰到死路 
        return

    # 如果有爸爸，就計算差值絕對值並累加 
    if parent_id is not None:
        total_diff += abs(current_id - parent_id)

    # 判斷奇偶數決定出口數量 
    if current_id % 2 == 1:
        # 奇數：3 個出口 (左、中、右)
        solve(current_id)
        solve(current_id)
        solve(current_id)
    else:
        # 偶數：2 個出口 (左、右)
        solve(current_id)
        solve(current_id)

# 從起點開始（起點沒有爸爸，設為 None）
solve(None)
print(total_diff)