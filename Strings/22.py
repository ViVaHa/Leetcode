class Solution:
    def generate(self,openBrackets,closedBrackets,isOpen,ans,temp):
        if openBrackets==0 and closedBrackets==0:
            ans.append(temp)
            return
        elif closedBrackets<openBrackets:
            return
        if openBrackets-1>=0:
            self.generate(openBrackets-1,closedBrackets,True,ans,temp+"(")
        if closedBrackets-1>=0:
            self.generate(openBrackets,closedBrackets-1,False,ans,temp+")")
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return None
        openBrackets=n
        closedBrackets=n
        ans=[]
        o=True
        temp=""
        self.generate(openBrackets-1,closedBrackets,o,ans,temp+"(")
        return ans
        
        
