class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def solve(i,temp,total):
            if total==target:
                res.append(list(temp))
                return
            if i>=len(candidates) or total>target:
                return
            temp.append(candidates[i])
            solve(i+1,temp,total+candidates[i])
            temp.pop()
            next_i=i+1
            while next_i<len(candidates) and candidates[next_i]==candidates[i]:
                next_i+=1
            solve(next_i,temp,total)
        solve(0,[],0)
        return res
        