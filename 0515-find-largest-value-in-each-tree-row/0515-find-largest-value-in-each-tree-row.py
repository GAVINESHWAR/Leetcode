# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        if root == None:
            return None
        
        qu = [root]
        max_el = []
        
        while len(qu) != 0:
            
            a = len(qu)
            maxm = float('-Inf')
            
            for i in range(a):
                
                node = qu[0]
                qu.pop(0)
                if node and node.val > maxm:
                    maxm = node.val
                if node and node.left:
                    qu.append(node.left)
                if node and node.right:
                    qu.append(node.right)
            max_el.append(maxm)
        
        return max_el
        
        