class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r= 0, len(nums)-1

        while(l<=r):
            mid = (l+r)//2
            if(target==nums[mid]):
                return mid
            #check if mid is in left portion
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]: 
                    #then send to right
                    l=mid+1
                else:
                    #stay in left
                    r=mid-1

            #else check if its in right
            else:
                if target<nums[mid] or target>nums[r]:
                    #send to left
                    r=mid-1
                else:
                    #stay in right
                    l=mid+1
        return -1
