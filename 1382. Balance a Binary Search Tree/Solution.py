from modules import TreeNode

def balanceBST(self, root: TreeNode) -> TreeNode:
    tree_values = []

    def inorderTrav(node: TreeNode) -> None:
        if node is None:
            return
        inorderTrav(node.left)
        tree_values.append(node.val)
        inorderTrav(node.right)

    inorderTrav(root)

    def buildBST(l: int, r: int) -> TreeNode:
        if l > r:
            return None
        m = (l + r) // 2
        return TreeNode(tree_values[m], 
                        buildBST(l, m - 1), 
                        buildBST(m + 1, r))

    return buildBST(0, len(tree_values) - 1)