class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # res=[0]*n
        # for i in range(n):
        #     prod=1
        #     for j in range(n):
        #         if i==j:
        #             continue
        #         prod*=nums[j]
        #     res[i]=prod
        # return res

        #prefix-suffix
        # n=len(nums)
        # res=[1]*n
        # prefix=1
        # for i in range(n):
        #     res[i]=prefix
        #     prefix*=nums[i]
        # suffix=1
        # for i in range(n-1,-1,-1):
        #     res[i]*=suffix
        #     suffix*=nums[i]
        # return res

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

      
        