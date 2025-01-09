def countWords(words:list,pref:str)->int:
    n = len(words)
    fin = 0
    for word in words:
        if len(word) >= len(pref) and word[:len(pref)] == pref:
            fin += 1
    return fin


if __name__ == '__main__':
    words = ["pay","attention", "practice","attention"]
    pref = "at"
    fin = 0
    for word in words:
        print(word[:len(pref)])
        if len(word) >= len(pref) and word[:len(pref)] == pref:
            print(word)
            fin += 1
    print(fin)
    print(countWords(words,pref))