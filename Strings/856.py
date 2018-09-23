class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack=[0]
        if len(S)==0:
            return 0
        i=0
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(0)
            else:
                inner=stack.pop()
                stack[-1]+=max(inner*2,1)
        return stack[0]
        
