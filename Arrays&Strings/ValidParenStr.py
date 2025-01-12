# 2116. Check if a parentheses string can be valid

def canBeValid(s:str,locked:str)->bool:
    n = len(s)
    if n % 2 != 0:
        print(False)
    oc = 0  # open braces count
    # Left to right traversal
    for i in range(n):
        if s[i] == "(" or locked[i] == "0":
            oc += 1
        else:
            oc -= 1
        if oc < 0:
            return(False)
    cc = 0  # Close braces count
    # Right to left traversal
    for i in range(n - 1, -1, -1):
        if s[i] == ")" or locked[i] == '0':
            cc += 1
        else:
            cc -= 1
        if cc < 0:
            return(False)
    return(True)


if __name__ == '__main__':
    print("Hello")
    s = "))()))"
    locked = "010100"
    n = len(s)
    if n % 2 != 0:
        print(False)
    oc = 0 #open braces count
    #Left to right traversal
    for i in range(n):
        if s[i] == "(" or locked[i] == "0":
            oc += 1
        else:
            oc -= 1
        if oc < 0:
            print(False)
    cc = 0 #Close braces count
    #Right to left traversal
    for i in range(n-1,-1,-1):
        if s[i] == ")" or locked[i] == '0':
            cc += 1
        else:
            cc -= 1
        if cc < 0:
            print(False)
    print(True)
    print(canBeValid(s,locked))