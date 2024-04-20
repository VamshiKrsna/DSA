array = [3,4,6,7,9,12,16,17]
sch = 8
# Linear Searching :
for i in range(0,len(array)):
    if array[i] == sch:
        print(f"{sch} found at {i}th index")

# Binary Search Approach
def BinSchIter(array,sch):
    l = 0
    r = len(array)-1
    while l<=r:
        m = (l+r)//2
        if array[m] == sch:
            print(f"{sch} found at {m}")
            break
        elif array[m] < sch:
            l = m+1
        else :
            r = m-1
    return -1

BinSchIter(array,sch)
if BinSchIter(array,sch) == -1:
    print("Not Found")

def BinSchRecursive(array,sch,l,r):
    m = (l+r)//2
    if r<l:
        return -1
    elif sch == array[m]:
        print(f"{sch} found at {m}")
    elif sch > array[m]:
        BinSchRecursive(array,sch,m+1,r)
    else:
        BinSchRecursive(array,sch,l,m-1)

BinSchRecursive(array,3,0,len(array))