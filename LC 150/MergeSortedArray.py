# LC 150 : 1. Merge Sorted Array
def merge(nums1,nums2,m,n):
    i,j,k = m-1,n-1,m+n-1
    while i>=0 and j>=0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i-=1
        else:
            num1[k] = num2[j]
            j-=1
        k -= 1
    while j>=0:
        nums1[k] = nums2[j]
        j-=1
        k-=1
    return nums1

if __name__ == "__main__":
    num1 = [1,2,3,0,0,0]
    num2 = [2,5,6]
    m, n = 3,3
    i,j,k = m-1,n-1,m+n-1
    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i-=1
        else:
            num1[k] = num2[j]
            j-=1
        k -= 1
    print(num1)
    print(merge(num1,num2,m,n))