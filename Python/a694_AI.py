import sys

def solve():
    # 一次性讀入所有輸入資料，並用 split() 切割成單純的字串陣列
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 使用 iterator 依序取出資料，效率最高
    iterator = iter(input_data)
    
    while True:
        try:
            # 讀取 n 和 m
            n_str = next(iterator)
            m_str = next(iterator)
        except StopIteration:
            break  # 讀取完畢，正常結束（符合 EOF 要求）
            
        n = int(n_str)
        m = int(m_str)
        
        # 建立 (n+1) * (n+1) 的前綴和陣列，預先補一圈 0 避免處理邊界問題
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        
        # 計算二維前綴和
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                val = int(next(iterator))
                # 關鍵公式：當前前綴和 = 上 + 左 - 左上 + 當前值
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + val
                
        # 處理 m 次範圍查詢
        output = []
        for _ in range(m):
            x1 = int(next(iterator))
            y1 = int(next(iterator))
            x2 = int(next(iterator))
            y2 = int(next(iterator))
            
            # O(1) 區間查詢公式：大矩形 - 上矩形 - 左矩形 + 左上重複扣掉的矩形
            ans = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
            output.append(str(ans))
            
        # 將該組測資的答案一次輸出，減少 I/O 耗時
        sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
