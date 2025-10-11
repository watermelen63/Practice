num1st, operation, num2nd = input().split()
n1, n2 = int(num1st), int(num2nd)
if operation == "+":
    print(n1 + n2)
elif operation == "-":
    print(n1 - n2)
elif operation == "*":
    print(n1 * n2)
else:
    print(n1 // n2)