# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

class Solution:
    def find_depth(self, node, depth:
        if node.left is None and node.right is None:
            return depth+1
        else:
            if node.left:
                self.find_depth(node.left, depth+1)
            if node.right:
                self.find_depth(node.right, depth + 1)
            
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.find_depth(root, 0)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_root(l):
    root = TreeNode(l[0])
    node = root
    for i in range(len(l)-1):
        if node is None:
            pass
        if i % 2 == 0:
            node.left = TreeNode(l[i])
        else:
            node.right = TreeNode(l[i])
    return root


s = Solution()
input = [3,9,20,None,None,15,7]
root = get_root(input)
print(root)

d = s.minDepth(root)
print(d)
