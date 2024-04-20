# Dutch National Flag Algorithm for 3 distinct values.

nums = [0,1,2,1,0,2,1,1,0,2]

low, mid = 0,0

high = len(nums)-1

while(mid<=high):
    if nums[mid] == 0:
        temp = nums[low]
        nums[low] = nums[mid]
        nums[mid] = temp
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        temp = nums[mid]
        nums[mid] = nums[high]
        nums[high] = temp
        high -= 1

print(nums) #[0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

