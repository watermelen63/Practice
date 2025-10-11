n = input('請輸入一串數字，我會將那串數字翻轉\n')
reversed_n = n[::-1]  # 字串反轉
result = reversed_n.lstrip('0')  # 去除開頭的0
if result == (""):
    result = 0
print(result)