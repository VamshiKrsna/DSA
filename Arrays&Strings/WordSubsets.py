from collections import Counter
def wordSubsets(words1:list,words2:list)->list:
    max_freq = Counter()
    for word in words2:
        max_freq |= Counter(word)
    fin = []
    for word in words1:
        freq = Counter(word)
        if all(freq[char] >= max_freq[char] for char in max_freq):
            fin.append(word)
    return fin

if __name__ == '__main__':
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    print(wordSubsets(words1,words2))