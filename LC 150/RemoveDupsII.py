def removedupsii(nums):
    counter = {}
    k = 0
    for num in nums:
        counter[num] = counter.get(num,0)+1
        if count[num] <= 2:
            nums[k] = num
            k+=1
    return k

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    count = {}
    k = 0
    for num in nums:
        count[num] = count.get(num,0)+1
        k+=1
    print(k)
    print(nums)
    print(removedupsii(nums))