# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, val: int, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: return True
        elif not p or not q: return False
        
        if p.val >= val or q.val <= val:
            return False
        return self.helper(p.val, p.left, p.right) and self.helper(q.val, q.left, q.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        return self.helper(root.val, root.left, root.right)



