class Solution(object):
    def postorder(self, root):
        ans = []

        def dfs(node):
            if not node:
                return

            # First visit all children
            for child in node.children:
                dfs(child)

            # Then visit the current node
            ans.append(node.val)

        dfs(root)

        return ans