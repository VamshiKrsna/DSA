# LC 34. Find First and Last Position of Element in Sorted Array
def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
