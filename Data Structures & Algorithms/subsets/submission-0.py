class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]

        def backtrack(i):
            if i==len(nums):
                res.append(sub.copy())
                return

            #include nums[i]
            sub.append(nums[i])
            backtrack(i+1)

            #exclude nums[i]
            sub.pop()
            backtrack(i+1)

        backtrack(0)
        return res
