class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        nums.sort()

        def back(i):
            res.append(sub.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                sub.append(nums[j])
                back(j+1)
                sub.pop()

        back(0)
        return res

                    
