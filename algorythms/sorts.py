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
            # print(step)
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
