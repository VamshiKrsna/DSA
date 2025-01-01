# Optimal Solution for max subarray for window size k :
# O(n) better than O(n*k)
def maxSumK(arr:list, n:int,k:int)->int:
    ws = sum(arr[:k])
    ms = ws
    for i in range(n-k):
        ws = ws-arr[i]+arr[i+k]
        ms = max(ws,ms)
    return ms

if __name__ == '__main__':
    arr = [1,4,2,10,2,31,0,20]
    print(maxSumK(arr,len(arr),4))