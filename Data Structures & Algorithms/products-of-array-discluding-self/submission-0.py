class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        prefix=1
        for i in range(n):
            left[i]*=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            right[i]*=suffix
            suffix*=nums[i]
        
        res=[]
        for i in range(n):
            res.append(left[i]*right[i])
        return res
