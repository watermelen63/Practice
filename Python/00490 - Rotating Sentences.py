first, second = input(), input()
if len(first) > len(second):
    second = second.ljust(len(first))
    for i in range(len(first)):
        print(second[i] + first[i])
elif len(second) > len(first):
    first = first.ljust(len(second))
    for i in range(len(second)):
        print(second[i] + first[i])