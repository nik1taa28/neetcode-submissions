class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                op2=int(stack.pop())
                op1=int(stack.pop())
                if i=='+':
                    res=op1+op2
                elif i=='-':
                    res=op1-op2
                elif i=='*':
                    res=op1*op2
                else:
                    res=op1/op2
                stack.append(res)
        return int(stack[0])