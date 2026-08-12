class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        res=0
        while r<len(nums)-1:
            max_range=0
            for i in range(l,r+1):
                max_range=max(max_range,i+nums[i])
            l=r+1
            r=max_range
            res+=1
        return res



        