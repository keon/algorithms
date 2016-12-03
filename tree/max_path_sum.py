
maximum = float("-inf")

def max_path_sum(root):
    helper(root)
    return maximum

def helper(root):
    if not root:
        return 0
    left = helper(root.left)
    right = helper(root.right)
    maximum = max(maximum, left+right+root.val)
    return root.val + max(left, right)
