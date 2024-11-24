def lengthOfLastWord(s: str) -> int:
    arr = s.split()
    return len(arr[-1])

if __name__ == '__main__':
    print(lengthOfLastWord("Hello World"))