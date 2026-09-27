def solve():
    tree_h = list(map(int, input().split()))
    height = int(input())

    num = 0
    for h in tree_h:
        if height + 30 >= h:
            num += 1
    print(num)


if __name__ == "__main__":
    solve()
