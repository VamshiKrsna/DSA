# 2270. Number Of Ways to Split Array
"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.



Example 1:

Input: nums = [10,4,-8,7]
Output: 2
Explanation:
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.
"""
def waysToSplit(nums:list)->int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    valid_splits = 0
    for i in range(n - 1):
        if prefix_sum[i + 1] >= prefix_sum[n] - prefix_sum[i + 1]:
            valid_splits += 1

    return valid_splits


def waysToSplit2(nums):
    pass

if __name__ == '__main__':
    nums = [10,4,-8,7]
    n = len(nums)
    # for i in range(n):
    #     # print(sum(nums[:i+1])) # first i+1 items
    #     # print(sum(nums[-(n-i-1):])) # Last n-i-1 items
    #     # print(nums[i+1:]) # items to the RHS of i
    #     fin = 0
    #     if sum(nums[:i+1]) >= sum(nums[-(n-i-1):]):
    #         print([return True if _ for _ in nums[i+1:] < n-1])
    print(waysToSplit(nums))