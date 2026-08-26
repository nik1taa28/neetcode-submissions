class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c=sorted(candidates)
        sub, res=[], []

        def comb(i,target):
            if target==0:
                res.append(sub.copy())
                return
            if target<0 or i>=len(c):
                return
            prev=-1

            for j in range(i,len(c)):
                if c[j]==prev:
                    continue
                sub.append(c[j])
                comb(j+1,target-c[j])
                sub.pop()
                prev=c[j]
        comb(0,target)
        return res
                
