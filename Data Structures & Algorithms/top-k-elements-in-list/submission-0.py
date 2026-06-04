class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        new=sorted(dict.items(),key=lambda x:x[1], reverse=True)
        res=[]
        for i in new[:k]:
            res.append(i[0])
        return res

        