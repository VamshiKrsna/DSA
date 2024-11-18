def removedups(nums):
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    # Method 1 :
    fin = []
    for i in nums:
        if i not in fin:
            fin.append(i)
    print(len(fin))
    # Method 2 :
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    print(i+1)