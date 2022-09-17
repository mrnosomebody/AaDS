class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f'{self.val}'

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val, end=' ')
        if self.right:
            self.right.printTree()


n, q = map(int, input().split(' '))
swaps = list(map(int, input().split(' ')))
tree_nodes = []

for i in range(1, n + 1):
    tree_nodes.append(TreeNode(i))

for i in range(n):
    if 2 * i + 1 >= n and 2 * i + 2 >= n:
        tree_nodes[i].left = None
        tree_nodes[i].right = None
    elif 2 * i + 1 < n and 2 * i + 2 >= n:
        tree_nodes[i].left = tree_nodes[2 * i + 1]
        tree_nodes[i].right = None
    else:
        tree_nodes[i].left = tree_nodes[2 * i + 1]
        tree_nodes[i].right = tree_nodes[2 * i + 2]
    if tree_nodes[i].left:
        tree_nodes[i].left.parent = tree_nodes[i]
    if tree_nodes[i].right:
        tree_nodes[i].right.parent = tree_nodes[i]


def dfs(root, target):
    if not root:
        return
    if target == tree_nodes[0].val:
        return
    if root.val == target:
        if root.parent == tree_nodes[0]:
            if root.parent.right == root:
                p = root.parent
                root.parent = None
                p.right = root.right
                if root.right:
                    root.right.parent = p
                p.parent = root
                root.right = p
                tree_nodes[0] = root
                return
            else:
                p = root.parent
                root.parent = None
                p.left = root.left
                p.parent = root
                if root.left:
                    root.left.parent = p
                root.left = p
                tree_nodes[0] = root
                return
        elif root.parent.right == root:
            root.parent.right = root.right
            if root.right:
                root.right.parent = root.right
            p = root.parent
            root.parent = p.parent
            if p.parent.right == p:
                root.parent.right = root
            else:
                root.parent.left = root
            root.right = p
            p.parent = root
            return
        else:
            root.parent.left = root.left
            if root.left:
                root.left.parent = root.parent
            p = root.parent
            root.parent = p.parent
            if p.parent.right == p:
                root.parent.right = root
            else:
                root.parent.left = root
            root.left = p
            p.parent = root
            return
    dfs(root.left, target)
    dfs(root.right, target)

for i in swaps:
    dfs(tree_nodes[0], i)
tree_nodes[0].printTree()