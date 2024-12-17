def basic_rev_array(nums):
    n = len(nums)
    l,r = 0,n-1
    while l < n/2 and r > n/2:
        swap(nums,l,r)
        l += 1
        r -= 1
    return nums


def swap(nums,i,j):
    # Swap in place only.
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def recursive_reverse_array(i,nums):
    n = len(nums)
    if i >= n/2:
        return
    swap(nums,i,n-i-1)
    recursive_reverse_array(i+1,nums)

if __name__ == '__main__':
    nums = [1,2,3,4,2]
    # print(swap(nums,0,-1))
    print(basic_rev_array(nums))
    print(recursive_reverse_array(0,nums))
    print(nums)