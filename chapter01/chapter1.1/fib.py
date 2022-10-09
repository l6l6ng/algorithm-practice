from typing import Dict
from functools import lru_cache
from typing import Generator

# memo: Dict[int, int] = {0: 0, 1: 1}
memo = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


@lru_cache(maxsize=None)
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


def fib3(n):
    if n == 0:
        return n

    last = 0
    next1 = 1

    for _ in range(1, n):
        last, next1 = next1, last + next1
    return next1


def fib4(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last = 0
    next1 = 1
    for _ in range(1, n):
        last, next1 = next1, last + next1
        yield next1


if __name__ == "__main__":
    # for i in range(10):
    # print(fib(i))
    # print(fib2(i))
    # print(fib3(i))
    for i in fib4(10):
        print(i)
