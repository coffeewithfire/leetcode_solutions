from modules import TreeNode

def convertBST(root: TreeNode) -> TreeNode:
    cur_sum = 0
    stk = []
    node = root
    while stk or node:
        while node:
            stk.append(node)
            node = node.right
        node = stk.pop()
        cur_sum += node.val
        node.val = cur_sum
        node = node.left
    return root