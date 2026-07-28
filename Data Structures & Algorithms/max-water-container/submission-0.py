class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        n=len(heights)
        ans=0
        r=n-1
        while i<r:
            w=r-i
            l=min(heights[i],heights[r])
            area=w*l
            ans=max(ans,area)
            if heights[i]>heights[r]:
                r-=1
            else:
                i+=1
     
        return ans


        