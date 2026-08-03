class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(left, node, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            # Left child: upper bound becomes node.val
            # Right child: lower bound becomes node.val
            return valid(left, node.left, node.val) and valid(node.val, node.right, right)
            
        return valid(float("-inf"), root, float("inf"))