nums=[-2,1,-3,4,-1,2,1,-5,4]
maxsum= nums[0]
curr=0
for i in nums:
    if curr<0:
        curr=0
    curr+=i
    maxsum=max(curr,maxsum)
print(maxsum)