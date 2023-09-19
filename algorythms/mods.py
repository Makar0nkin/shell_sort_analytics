import math
from functools import cache

number = int | float

@cache
def h2(self, k: int) -> int:
    t = math.log(self.n, 2) - 1
    if k > t:
        return 0
    elif k == t:
        return 1
    else:
        return 2 * h2(self, k + 1) + 1

@cache
def h3(self, k: int) -> int:
    t = math.log(self.n, 3) - 1
    if k > t:
        return 0
    elif k == t:
        return 1
    else:
        return 3 * h3(self, k + 1) + 1

@cache
def h_epx(self, k: int) -> int:
    # можно было использовать мемоизацию или что-то такое, но оно вроде не слильно влияет на производительность
    res: list = [int((2 ** i - (-1) ** i) / 3) for i in range(1, int(math.log(self.n, 2)) + 1)]
    return res[-k] if len(res) >= k + 1 is not None else 0


@cache
def fib(n: int):
    res = [0, 1]
    while res[-1] < n / 2:
        res.append(res[-1] + res[-2])
    return res

@cache
def h_fib(self, k: int) -> int:
    return fib(self.n)[-k]




