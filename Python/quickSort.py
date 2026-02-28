import timeit
import random

def quickSort(array):
    if len(array) <= 1:
        return array
    
    Pivot = array[0]

    left, right = [], []

    for i in array[1:]:
        if i < Pivot:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left) + [Pivot] +quickSort(right)

n = [random.randint(1, 100000) for _ in range(10000)]

print(quickSort(n))
print(f"目前程式運行了{timeit.timeit()}秒")