class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        n=len(prices)
        ans=0
        while r<n:
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                ans=max(ans,profit)
            else:
                l=r
            r+=1
        return ans


        