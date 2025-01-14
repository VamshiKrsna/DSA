# 2657. Prefix common array of two arrays  :
from typing import  List
def prefComm(A:List, B:List)->List:
    fin = []
    for i in range(1, len(A) + 1):
        a_sub = A[:i]
        b_sub = B[:i]
        temp_count = 0
        for j in range(i):
            if a_sub[j] in b_sub:
                temp_count += 1
        fin.append(temp_count)
    return fin


if __name__ == '__main__':
    # A = [1,3,2,4]
    # B = [3,1,2,4]
    A = [2,3,1]
    B = [3,1,2]
    fin = []
    for i in range(1,len(A)+1):
        a_sub = A[:i]
        b_sub = B[:i]
        print(a_sub)
        print(b_sub)
        temp_count = 0
        for j in range(i):
            if a_sub[j] in b_sub:
                temp_count += 1
        fin.append(temp_count)
        print(temp_count)
        print(fin)
    print(prefComm(A,B))