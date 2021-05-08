# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        '''
        
        
        Valid BST: 
            - left child < root 
            - right child > root 
            
            
            
            - traverse from the root. 
            - check if left child is less than the root. 
                - stop until you hit none 
            - check if right child is greater than the root. 
                - stop until you hit none. 
                
                
            helper method()
            
            #Base Case 
            if the node is pointing to none
                return True
                
                
            helper method to the left 
              if breaks return False 
            
            helper method to the right
                if breaks return False
            
            
            return True
            
            
            trigger helper
            
           
        
        '''
   
        
        def helper_method(node, lower = float('-inf'), upper = float('inf')):
            
            if not node:
                return True
            
            
            if lower >= node.val or upper<=node.val:
                return False
            if not helper_method(node.right, node.val, upper):
                return False
            if not helper_method(node.left, lower, node.val):
                return False
            return True
            
            
        return helper_method(root)
