import sys


def cycle_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def main():
    data = sys.stdin.buffer.read().decode("utf-8-sig").split()
    if not data:
        return

    values = list(map(int, data))
    for idx in range(0, len(values), 2):
        i, j = values[idx], values[idx + 1]
        start, end = sorted((i, j))
        max_len = 0

        for k in range(start, end + 1):
            max_len = max(max_len, cycle_length(k))

        print(i, j, max_len)


if __name__ == "__main__":
    main()