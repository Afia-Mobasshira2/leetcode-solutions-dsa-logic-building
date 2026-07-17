class Solution(object):
    def checkTree(self, root):
        # We access the number values using .val
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False