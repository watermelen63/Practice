n = int(input())

for i in range(n):
    seqeunce = list(map(int, input().split()))

    if seqeunce[1] - seqeunce[0] == seqeunce[2] - seqeunce[1]:
        seqeunce.append(seqeunce[3] + seqeunce[1] - seqeunce[0])
        for j in seqeunce:
            print(j, end = ' ')

    else:
        seqeunce.append(int(seqeunce[3] * (seqeunce[1] / seqeunce[0])))
        for j in seqeunce:
            print(j, end = ' ')

    print()