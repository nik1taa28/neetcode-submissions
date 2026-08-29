class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def back(openn,closen):
            if openn==closen==n:
                res.append("".join(stack))
                return
            if openn<n:
                stack.append('(')
                back(openn+1,closen)
                stack.pop()
            if closen<openn:
                stack.append(')')
                back(openn,closen+1)
                stack.pop()

        back(0,0)
        return res
            