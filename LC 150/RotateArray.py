# LC 6/150 : Rotate Array
from collections import deque
def rotate(nums,k):
    k %= len(nums)
    swapper(nums, 0, len(nums)-1)
    swapper(nums, 0, k-1)
    swapper(nums, k, len(nums)-1)
    return nums
def swapper(nums, beg, end):
    while beg < end:
        nums[beg], nums[end] = nums[end], nums[beg]
        beg += 1
        end -= 1

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    # Method 1 : Using Deque
    dk = deque(nums)
    print(dk)
    for i in range(k):
        dk.appendleft(dk[-1])
        dk.pop()
    print(dk)

    # Method 2 : Using Extra Space :
    temp = nums
    k %= len(nums) # To handle larger k easily
    temp[:] = temp[-k:] + temp[:-k]
    print(temp)

    # Method 3 : using recursive function (Optimal)
    temp = nums
    k = 3
    def swapper(nums, beg, end):
        while beg < end:
            nums[beg],nums[end] = nums[end],nums[beg]
            beg += 1
            end -= 1
    k %= len(temp)
    swapper(temp, 0, len(nums)-1)
    swapper(temp, 0, k-1)
    swapper(temp, k, len(nums)-1)
    print(temp)

    print(rotate(nums, k))