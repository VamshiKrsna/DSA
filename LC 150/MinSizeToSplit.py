nums = [2,4,8,2]
maxops = 4
l, r = 1, max(nums)
while l < r:
    m = (l+r)>>1 # average of l,r
    count = sum((x-1)//m for x in nums)
    if count <= maxops :
        r = m
    else:
        l = m+1
print(r)