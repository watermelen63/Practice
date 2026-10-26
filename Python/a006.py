from math import sqrt
a, b, c = map(int, input().split())
d = b ** 2 - 4 * a * c
logic = 1

if d > 0:
    print("Two different roots", end = ' ')

elif d == 0:
    print("Two same roots", end = ' ')
    logic = 2

else:
    print("No real root")
    logic = 0

if logic == 1:
    x1 = round((-b + sqrt(d)) / (2 * a))
    x2 = round((-b - sqrt(d)) / (2 * a))
    if x1 < x2:
        x1, x2 = x2, x1
    print(f"x1={x1} , x2={x2}")

elif logic == 2:
    print(f"x={int((-b + sqrt(d)) / (2 * a))}")