class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []
        if not root:
            return result

        queue = collections.deque([root])
        stack = []

        while queue or stack:

            result.append([])
            
            if len(queue) > 0:
                level_size = len(queue)
                for _ in range(level_size):
                    node = queue.popleft()
                    result[-1].append(node.val)

                    if node.left:
                        stack.append(node.left)

                    if node.right:
                        stack.append(node.right)
            
            else:
                level_size = len(stack)
                for _ in range(level_size):
                    node = stack.pop()
                    result[-1].append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

        return result