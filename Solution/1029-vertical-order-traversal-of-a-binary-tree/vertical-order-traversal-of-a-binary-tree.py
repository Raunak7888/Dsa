# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.in_order = []
        self.traverse(root, 0, 0)
        self.in_order.sort()

        prev_col = float("-inf")
        res = []
        for col, row, val in self.in_order:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)
        
        return res

    def traverse(self, node: TreeNode, row: int, col: int):
        if not node:
            return
        
        self.traverse(node.left, row+1, col-1)
        self.in_order.append((col, row, node.val))
        self.traverse(node.right, row+1, col+1)