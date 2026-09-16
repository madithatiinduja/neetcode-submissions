class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!= 1 and n not in seen:
            seen.add(n)
            ans=0
            for char in str(n):
                digit=int(char)
                ans+=digit**2
            n=ans
        return n==1
