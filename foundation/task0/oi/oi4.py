import math


def is_su(n: int):
    # N 确保大于等于 17，所以不需要做额外处理
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    n = int(input())
    if is_su(n):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
