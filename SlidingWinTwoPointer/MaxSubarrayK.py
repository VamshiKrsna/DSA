# Maximum subarray sum of window size k :
# O(n*k) solution
import sys
INT_MIN = -sys.maxsize - 1 #(-inf)
def maxSubSumK(arr:list,n:int,k:int)->int:
    """
    :param arr: array of numbers
    :param n: len of array
    :param k: window size
    :return: maximum sum in subarray of len k
    """
    max_sum = INT_MIN
    for i in range(n - k + 1):
        cs = 0
        for j in range(k):
            cs += arr[i+j]
        max_sum = max(cs, max_sum)
    return max_sum

if __name__ == '__main__':
    arr = [1,4,2,10,2,3,1,0,20]
    print(maxSubSumK(arr,len(arr),4))