# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxVal=0
    def getMaxPath(self,root):
        if root is None:
            return 0
        l=self.getMaxPath(root.left)
        r=self.getMaxPath(root.right)
        single=max(max(l,r)+root.val,root.val)
        val=max(l+r+root.val,single)
        if val>self.maxVal:
            self.maxVal=val
        return single
            
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxVal=-sys.maxsize
        if root is None:
            return 0
        value=self.getMaxPath(root)
        return self.maxVal
        
        
