def firstOccurence(haystack,needle):
    n = len(needle)
    if len(haystack) < n:
        return -1
    for i in range(len(haystack) - n):
        if haystack[i:i + n] == needle:
            return(i)
    return -1

if __name__ == '__main__':
    haystack = "leetcode"
    needle = "leeto"
    n = len(needle)
    for i in range(len(haystack)-n):
        if haystack[i:i+n] == needle:
            print(i)
        else: print(-1)
    print(firstOccurence(haystack,needle))