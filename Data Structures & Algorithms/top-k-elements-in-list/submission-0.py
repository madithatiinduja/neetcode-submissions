from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        cnt=list(count.values())
        cnt.sort(reverse=True)
        top_k=cnt[:k]
        res=[]
        for key,value in count.items():
            if value in top_k:
                res.append(key)
        return res

                

        