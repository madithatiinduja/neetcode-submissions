class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''res=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet=tuple(sorted((nums[i],nums[j],nums[k])))
                        res.append(triplet)
        return list(set(res))'''
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    res.append((nums[i],nums[j],nums[k]))
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1

                    j+=1
                    k-=1
        return res

