dic = {'+':1,'-':1,'*':2,'/':2}
def change(arr):
    stack, output = [], []
    for i in arr:
        if i.isdigit():output.append(i)
        elif i == '(':stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and dic[i] <= dic[stack[-1]]:
                output.append(stack.pop())
            stack.append(i)
    while stack:
        output.append(stack.pop())
    return output

def mergeNum(arr):
    output = []
    temp_num = ''
    for i in arr:
        if i.isdigit():temp_num += i
        else:
            if temp_num != '':
                output.append(temp_num)
                temp_num = ''
            if i != ' ':
                output.append(i)

    if temp_num:
        output.append(temp_num)

    return output

n = list(input())

ans = change(mergeNum(n))

for i in ans:
    print(i, end = ' ')