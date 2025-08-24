def inorder(root):
    if root ==  None:
        return

    inorder(root.left)
    print(root, end = " ")
    inorder(root.right) 