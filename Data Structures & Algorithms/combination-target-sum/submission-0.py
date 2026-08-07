class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def solve(i,cur,total):
            if total==target:
                res.append(list(cur))
                return
            if i>=len(nums) or total>target:
                return
            cur.append(nums[i])
            solve(i,cur,total+nums[i])
            cur.pop()
            solve(i+1,cur,total)
        cur=[]
        solve(0,cur,0)
        return res
        