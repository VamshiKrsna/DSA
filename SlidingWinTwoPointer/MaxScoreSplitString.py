def maxScore(s:str)->int:
    fin = []
    for i in range(1,len(s)):
        lss = s[:i]
        rss = s[i:]
        fin.append(lss.count("0") + rss.count("1"))
    return max(fin)

def maxScoreOptimal(s:str)->int:
    l,r,ans = 0,0,0
    for i in range(len(s)):
        if s[i] == "1":
            r += 1
    for i in range(len(s)-1):
        if s[i] == "1":
            r -= 1
        else : l += 1
        ans = max(ans, l+r)
    return ans

if __name__ == '__main__':
    s = "011101"
    fin = []
    for i in range(1,len(s)):
        # print(s[:i])
        # print(s[i:])
        # print("\n")
        lss = s[:i]
        rss = s[i:]
        fin.append(lss.count("0") + rss.count("1"))
    print(fin)
    print(max(fin))
    print(maxScore("011101"))
    print(maxScoreOptimal("011101"))