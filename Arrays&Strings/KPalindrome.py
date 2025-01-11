def canConstruct(s: str, k: int) -> bool:
    if len(s) == k:
        return True
    if len(s) < k:
        return False
    odd = 0
    for char in set(s):
        if s.count(char) % 2:
            odd += 1
    if odd > k:
        return False
    return True


if __name__ == '__main__':
    s = "annabelle"
    k = 2
    print(canConstruct(s,k))