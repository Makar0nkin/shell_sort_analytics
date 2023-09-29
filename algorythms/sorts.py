from typing import Callable
from algorythms.mods import h2, h3, h_epx, h_fib


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


class ShellSort:
    def __init__(self, h_logic: Callable[[object, int], int]):
        self.h_logic = h_logic  # increment function
        self.n = 0  # array length

    def h(self, k):
        return self.h_logic(self, k)

    def sort(self, arr):
        self.n = len(arr)
        counter = 1
        step = self.h(counter)
        while step > 0:
            counter += 1
            for i in range(step, self.n, 1):
                j = i
                delta = j - step
                while delta >= 0 and arr[delta] > arr[j]:
                    arr[delta], arr[j] = arr[j], arr[delta]
                    j = delta
                    delta = j - step
            step = self.h(counter)
        return arr


shell_sort_base = ShellSort(lambda self, k: self.n // 2 ** k).sort
shell_sort_h2 = ShellSort(h2).sort
shell_sort_h3 = ShellSort(h3).sort
shell_sort_exp = ShellSort(h_epx).sort
shell_sort_fib = ShellSort(h_fib).sort


def comb_sort(arr):
    operation_counter = 3
    gap = len(arr)
    swaps = True
    while gap > 1 or swaps:
        operation_counter += 6
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(arr) - gap):
            j = i + gap
            operation_counter += 6
            if arr[i] > arr[j]:
                operation_counter += 6
                arr[i], arr[j] = arr[j], arr[i]
                swaps = True
    return arr, operation_counter


def quick_sort(arr, operation_counter: int = 0):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        operation_counter += 1
        return arr, operation_counter
    else:
        pivot = arr[0]
        operation_counter += 1
        for i in arr:
            operation_counter += 3
            if i < pivot:
                operation_counter += 2
                less.append(i)
            elif i > pivot:
                operation_counter += 4
                more.append(i)
            else:
                operation_counter += 6
                pivotList.append(i)
        less, add_op = quick_sort(less)
        operation_counter += add_op + 2
        more, add_op = quick_sort(more)
        operation_counter += add_op + 2
        return less + pivotList + more, operation_counter


def bucket_sort(arr):
    operation_counter = 0
    bucket = []

    # Create empty buckets
    operation_counter += 2 * len(arr)
    for i in range(len(arr)):
        bucket.append([])

    # Insert elements into their respective buckets
    operation_counter += 3 * len(arr)
    for j in arr:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    operation_counter += len(arr)
    for i in range(len(arr)):
        bucket[i], add_op = comb_sort(bucket[i])
        operation_counter += add_op

    # Get the sorted elements
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
            operation_counter += 5
    return (arr, operation_counter)
