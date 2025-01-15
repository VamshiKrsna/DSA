def minimizeXor(num1: int, num2: int) -> int:
    bits = countSet(num2)
    fin = 0
    for i in range(31, -1, -1):
        if bits > 0 and (num1 & (1 << i)):
            fin |= (1 << i)
            bits -= 1
    for i in range(32):
        if bits > 0 and not (fin & (1 << i)):
            fin |= (1 << i)
            bits -= 1
    return fin


def countSet(n: int) -> int:
    fin = 0
    while n:
        fin += n & 1
        n >>= 1
    return fin

if __name__ == '__main__':
    num1 = 3
    num2 = 5
    print(minimizeXor(num1,num2))