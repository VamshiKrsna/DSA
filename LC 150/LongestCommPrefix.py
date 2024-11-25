def longcommpref(strings):
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            print(ans)
        ans += first[i]
    print(ans)

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            print(ans)
        ans += first[i]
    print(ans)
    longcommpref(strs)