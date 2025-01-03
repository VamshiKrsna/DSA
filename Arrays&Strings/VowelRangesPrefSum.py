# 2559. Count Vowel Strings in Ranges :
# Prefix Sum, Range Sum Problem : String + Array Variation :

def prefsum(words:list,queries:list)->list:
    vowels = "aeiou"
    fin = [] # Stores no. of words that start and end with vowel in a range
    for query in queries:
        upd = 0
        for i in range(min(query), max(query) + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                upd += 1 # Add if string start and end with a vowel
        fin.append(upd)
    return fin


if __name__ == '__main__':
    print("Hello World")
    # words = ["aba", "bcb", "ece", "aa", "e"]
    # vowels = "aeiou"
    # queries = [[0, 2], [1, 4], [1, 1]]
    # Works good.
    words = ["a","e","i"]
    vowels = "aeiou"
    queries = [[0, 2], [0, 1], [2, 2]]
    fin = []
    for query in queries:
        upd = 0
        for i in range(min(query),max(query)+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                upd += 1
        fin.append(upd)
    print(fin)