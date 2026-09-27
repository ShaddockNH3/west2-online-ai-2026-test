def is_run(year: int):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def solve():
    start, end = map(int, input().split())
    for year in range(start, end + 1):
        if is_run(year):
            print(year, end=" ")
        year += 1
    print()


if __name__ == "__main__":
    solve()
