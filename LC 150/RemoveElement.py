def removeElement(nums,val):
    temp = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[temp] = nums[i]
            temp += 1
    return temp
if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 2
    idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[idx] = nums[i]
            idx += 1
    print(idx)
    print(removeElement(nums,val))