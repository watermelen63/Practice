def factorial(x):
    if x < 0:
        raise ValueError("x 不能小於 0")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def P(n, r):
    if r < 0 or n < 0 or r > n:
        raise ValueError("請輸入 0 <= r <= n")
    return factorial(n) // factorial(n - r)


while True:
    try:
        n, r = map(int, input().split())
        print(P(n, r))
    except EOFError:
        break
    except ValueError as e:
        print(e)