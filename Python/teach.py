n = int(input())
if n % 2 == 0 and n % 3 == 0:
    print("6")
else:
    if n % 2 == 0 or n % 3 == 0:
        print("2,3")
    else:
        print("no")