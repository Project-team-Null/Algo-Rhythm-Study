from sys import stdin

def preorder(tree, node):
    if node == '.': return
    print(node, end="")
    for child in tree[node]:
        preorder(tree, child)


def inorder(tree, node):
    if node == '.': return
    inorder(tree, tree[node][0])
    print(node, end="")
    inorder(tree, tree[node][1])


def postorder(tree, node):
    if node == '.': return
    for child in tree[node]:
        postorder(tree, child)
    print(node, end="")


if __name__ == '__main__':
    read = stdin.readline
    n= int(read().rstrip())
    tree = {}
    for _ in range(n):
        slf, left, right = read().rstrip().split()
        tree[slf] = [left, right]
    
    preorder(tree, 'A')
    print()
    inorder(tree, 'A')
    print()
    postorder(tree, 'A')