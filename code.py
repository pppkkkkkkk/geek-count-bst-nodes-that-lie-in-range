'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def getCount(self, root, l, h):
        # Your code here
        
        cnt = 0 
        
        def dfs(node, l, h):
            nonlocal cnt
            if not node:
                return
            if node.data >= l and node.data <= h:
                cnt+=1
            if node.data > l:
                dfs(node.left, l, h)
            if node.data < h:
                dfs(node.right, l, h)
            
        dfs(root, l, h)
        
        return cnt