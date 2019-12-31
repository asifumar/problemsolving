class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        depth = 1
        return max(depth, self.findDepth(root.left, depth), self.findDepth(root.right, depth))

    def findDepth(self, root: TreeNode, depth: int) -> int:
        if root is None:
            return 0
        else:
            depth += 1
            return max(depth, self.findDepth(root.left, depth), self.findDepth(root.right, depth))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left = TreeNode(20)

test = Solution()
print(test.maxDepth(root))

