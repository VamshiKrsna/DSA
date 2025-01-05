# 1003: Check if the word is valid after substitutions:

def isValid(s:str)->bool:
    stk = []
    for i in s:
        if i == "c":
            if stk[-2:] != ['a','b']:
                return False
            stk.pop()
            stk.pop()
        else:
            stk.append(i)
    return not stk

if __name__ == '__main__':
    s = "aabcbc"
    stk = []
    for i in s:
        if i == "c":
            if stk[-2:] != ['a','b']:
                print(False)
            stk.pop()
            stk.pop()
        else:
            stk.append(i)
    print(not stk)