s, h, w = input('性別Male or Female(以 M or F 輸入)'), int(input()), int(input())
h /= 100
BMI = w / (h ** 2)
while True:
    if s == "M" or s == "F":
        if s == 'M':
            if BMI < 22:
                print("過輕")
            elif BMI <= 25 and BMI >= 22:
                print("理想體重")
            else:
                print("超重")
        if s == 'F':
            if BMI < 18:
                print("過輕")
            elif BMI >= 18 and BMI <= 22:
                print("理想體重")
            else:
                print("超重")
        break
    else:
        print("input incorrect")
        continue