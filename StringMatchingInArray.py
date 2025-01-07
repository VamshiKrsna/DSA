# 1408. String Matching in an Array

def stringMatch(words:list)->list:
    n = len(words)
    fin = []
    for i in range(n):
        for j in range(n):
            if i != j and words[j].find(words[i]) != -1:
                fin.append(words[i])
                break
    return fin

if __name__ == '__main__':
    print("hello")
    words = ["mass", "as", "hero", "superhero"]
    print(stringMatch(words))