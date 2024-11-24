def romantoint(s:str)->int:
    rti = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    for i in range(len(s) - 1):
        if rti[s[i]] < rti[s[i + 1]]:
            ans -= rti[s[i]]
        else:
            ans += rti[s[i]]
    return(ans + rti[s[-1]])

if __name__ == '__main__':
    # s = "LVIII"
    s = "MCMXCIV"
    rti = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    ans = 0
    for i in range(len(s)-1):
        if rti[s[i]] < rti[s[i+1]]:
            ans -= rti[s[i]]
        else:
            ans += rti[s[i]]
    print(ans + rti[s[-1]])
    print(romantoint(s))