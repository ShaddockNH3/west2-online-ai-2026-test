def solve() -> None:
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            print(f"{i} * {j} = {i * j}", end=" ")
            j += 1
        i += 1
        print()


if __name__ == "__main__":
    solve()
