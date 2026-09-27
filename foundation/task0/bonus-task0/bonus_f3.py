# 输入⼀个字符串，判断字符串中是否含有 "ol" 这个⼦串，若有把所有的 "ol" 替换为 "fzu"，最后把字符串倒序输出


def solve() -> None:
    str_a = input()
    if "ol" in str_a:
        str_a: str = str_a.replace("ol", "fzu")
    # 倒序输出字符串
    print(str_a[::-1])


if __name__ == "__main__":
    solve()
