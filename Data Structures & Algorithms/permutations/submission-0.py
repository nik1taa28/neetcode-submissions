class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        vis=[False]*len(nums)
        def back(perm,nums,vis):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not vis[i]:
                    perm.append(nums[i])
                    vis[i]=True
                    back(perm,nums,vis)
                    perm.pop()
                    vis[i]=False
        back(perm,nums,vis)
        return res