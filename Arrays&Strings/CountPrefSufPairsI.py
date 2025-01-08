# 3042. Count Prefix and Suffix Pairs I
def countPairs(words:list)->int:
    fin = 0
    for i in range(len(words)):
        for j in range(i,len(words)):
            l,r = words[i],words[j]
            if len(l) >= len(r):
                continue
            nl = len(l)
            if l == r[:nl] and l == r[-nl:]:
                fin += 1
    return fin

def isPrefAndSuf(word1,word2):
    n1,n2 = len(word1),len(word2)
    if n1 > n2:
        return False
    return word2[:n1] == word1 and word2[-n1:] == word1

def countPairsOpt(words:list)->int:
    n = len(words)
    fin = 0
    for i in range(n):
        for j in range(i+1,n):
            if isPrefAndSuf(words[i],words[j]):
                fin += 1
    return fin


if __name__ == '__main__':
    # words = ["a","aba","ababa","aa"]
    fin = 0
    words = ["a","abb"]
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            l = words[i]
            r = words[j]
            if len(l) >= len(r):
                continue
            nl = len(l)
            # nr = len(r)
            print(l)
            print(r)
            print(r[:nl])
            print(r[-nl:])
            print('\n')
            if l == r[:nl] and l == r[-nl:]:
                fin += 1
            print(fin)

        print(countPairs(words))
    print(countPairsOpt(words))