class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        curr=1
        long=1
        if not nums:
            return 0 
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr+=1
            else:
                long=max(curr,long)
                curr=1
        return max(long,curr)

        