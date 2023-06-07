#!/usr/bin/python3
root = int, input()

def maxDepth(self, root: 'Node') -> int:
        
        stack = []
        if root:
            stack.append((root, 1))
        depth = 0
        while stack:
            (node, level) = stack.pop()
            depth = max(depth, level)
            for child in node.children:
                stack.append(child)

        return depth