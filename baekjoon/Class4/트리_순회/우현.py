from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    n = int(read())
    tree = dict()
    for _ in range(n):
        par, left, right = read().rstrip().split()
        tree[par] = [left, right]

    def preoder(node):
        print(node, end='')
        for c in tree[node]:
            if c != '.':
                preoder(c)

    def inorder(node):
        if tree[node][0] != '.':
            inorder(tree[node][0])
        print(node, end='')
        if tree[node][1] != '.':
            inorder(tree[node][1])

    def postorder(node):
        if tree[node][0] != '.':
            postorder(tree[node][0])
        if tree[node][1] != '.':
            postorder(tree[node][1])
        print(node, end='')

    preoder("A")
    print()
    inorder("A")
    print()
    postorder("A")
