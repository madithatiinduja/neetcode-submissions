class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        n=len(height)
        r=n-1
        ans=0
        leftmax=height[l]
        rightmax=height[r]
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(height[l],leftmax)
                ans+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(height[r],rightmax)
                ans+=rightmax-height[r]
        return ans


        

        