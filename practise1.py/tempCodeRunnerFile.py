def find(root):
    if root.left is None:
        if root.right:
            while root.left:
                list.append(root.left)
        else:
            return
    while root.left:
        list.append(root.left)