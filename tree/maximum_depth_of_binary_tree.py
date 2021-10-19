"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n), Space: O(n)
class Solution:
    """
    Recursive Depth-First Search:

    This solution takes a recursive approach by counting how deep each node goes
    with a node having no children being an exit condition. By comparing if the
    depth of the left node to the right node we can only consider the deepest
    part of the tree.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Time: O(n), Space: O(n)
class Solution:
    """
    Iterative Depth-First Search:
    
    This solution uses a stack to process all children nodes before its
    siblings. It can then compare the depth of each traversal and store the
    maximum. This particular solution traverses to the right first. Stacks
    process data in a first in, last out fashion.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)  
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return max_depth

# Time: O(n), Space: O(n)
class Solution:
    """
    Iterative Breadth-First Search:
    
    This solution uses a queue to process all sibling nodes before its children.
    If a node has children then its children are added to the queue. Nodes are
    removed from the queue after being processed. Queues process data in a first
    in, first out fashion.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        q = [root]
        while q:

            for i in range(len(q)):
                node = q.pop(0)

                if node.left:   
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            depth += 1
        
        return depth