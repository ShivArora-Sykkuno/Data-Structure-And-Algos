def preorder(root):
    if root ==  None:
        return
    print(root, end = " ")
    preorder(root.left)
    preorder(root.right) 