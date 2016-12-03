
def array2bst(nums):
    if not nums:
        return None
    mid = len(nums)//2
    node = Node(nums[mid])
    node.left = array2bst(nums[:mid])
    node.right = array2bst(nums[mid+1:])
    return node
