class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        def sub(index,target):
            if target==0:
                return True
            if index>=len(nums) or target<0:
                return False
            if (index,target) in memo: 
                return memo[(index,target)]
            res=sub(index+1,target-nums[index]) or sub(index+1,target)
            memo[index,target]=res
            return res
        return sub(0,target)
        