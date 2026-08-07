class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(i,temp,nums):
            if i==len(nums):
                res.append(list(temp))
                return
            temp.append(nums[i])
            solve(i+1,temp,nums)
            temp.pop()
            solve(i+1,temp,nums)
        temp=[]
        solve(0,temp,nums)
        return res

        