def print_factors(n, j=1):
    if j > n:
        return
    if j < n:
        if n % j == 0:
            print(j, end=' ')
    else:  # j == n
        print(n, end='\n')
    print_factors(n, j + 1)

n = int(input())
print_factors(n)