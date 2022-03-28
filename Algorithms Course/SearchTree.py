from collections import deque

# RED BLACK TREE IMPLEMENTATION
# Current problems
#   1. Tree must have at least one element (Root cannot be removed)
#       -> Delete and Insert should be improved
#   2. Exception handling for deleting elements not in tree.


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftchild = None
        self.rightchild = None 


class BinarySearchTree:
    NIL = Node(None)

    def __init__(self, key):
        self.root = Node(key)
        self.root.leftchild = self.NIL
        self.root.rightchild = self.NIL

    def printTree(self):
        self.inorderTraverse(self.root); print()
        self.levelorderTraverse(deque([self.root]))
        
    def inorderTraverse(self, node):
        if node == self.NIL: return
        self.inorderTraverse(node.leftchild)
        print(node.key, end = " ")
        self.inorderTraverse(node.rightchild)

    def levelorderTraverse(self, que):
        while len(que) != 0:
            l = len(que)
            for _ in range(l):
                cur = que.popleft()
                print(cur.key, end = "/")
                if cur.parent: print(cur.parent.key, end = "/")
                print(cur.black, end = " ")
                if cur.leftchild != self.NIL: que.append(cur.leftchild)
                if cur.rightchild != self.NIL: que.append(cur.rightchild)
            print()

    def find(self, key):
        ret = self.treeSearch(self.root, key)
        return ret.key

    def insert(self, key):
        r = Node(key); r.leftchild = self.NIL; r.rightchild = self.NIL
        self.treeInsert(self.root, r)

    def delete(self, key):
        target = self.treeSearch(self.root, key)
        if target.leftchild != self.NIL and target.rightchild != self.NIL:
            temp = self.successor(target)
            target.key = temp.key
            target = temp
        self.treeDelete(target)

    def treeSearch(self, node, key):
        if node.key == None or node.key == key: return node
        if key < node.key: return self.treeSearch(node.leftchild, key)
        else: return self.treeSearch(node.rightchild, key)

    def treeInsert(self, node, r):
        if node.key == r.key: return node
        if node.key == None:
            return r
        if r.key < node.key:
            temp = self.treeInsert(node.leftchild, r)
            node.leftchild = temp
            temp.parent = node
            return node
        else:
            temp = self.treeInsert(node.rightchild, r)
            node.rightchild = temp
            temp.parent = node
            return node

    def successor(self, node):
        temp = node.rightchild
        while temp.leftchild != self.NIL:
            temp = temp.leftchild
        return temp

    def treeDelete(self, node):
        if node.leftchild == self.NIL and node.rightchild == self.NIL:
            p = node.parent
            if node == p.leftchild: p.leftchild = self.NIL
            else: p.rightchild = self.NIL
        elif node.leftchild == self.NIL:
            p = node.parent
            node.rightchild.parent = p
            if node == self.root:
                self.root = node.rightchild
                return
            if node == p.leftchild: p.leftchild = node.rightchild
            else: p.rightchild = node.rightchild
        else:
            p = node.parent
            node.leftchild.parent = p
            if node == self.root:
                self.root = node.leftchild
                return
            if node == p.leftchild: p.leftchild = node.leftchild
            else: p.rightchild = node.leftchild


class rbNode(Node):
    def __init__(self, key, b):
        super().__init__(key)
        self.black = b


class RedBlackTree(BinarySearchTree):
    NIL = rbNode(None, True)

    def __init__(self, key):
        self.root = rbNode(key, True)
        self.root.leftchild = self.NIL
        self.root.rightchild = self.NIL

    def printBlackHeight(self, node, d):
        if node.black: d = d+1
        if node.leftchild == self.NIL and node.rightchild == self.NIL:
            print(d, end = " ")
        if node.leftchild != self.NIL: self.printBlackHeight(node.leftchild, d)
        if node.rightchild != self.NIL: self.printBlackHeight(node.rightchild, d)

    def rotateLeft(self, x, y):
        p = x.parent
        y.leftchild.parent = x
        x.rightchild = y.leftchild
        y.parent = p
        x.parent = y
        y.leftchild = x
        if x == self.root: self.root = y
        else:
            if x == p.leftchild: p.leftchild = y
            else: p.rightchild = y

    def rotateRight(self, x, y):
        p = y.parent
        x.rightchild.parent = y
        y.leftchild = x.rightchild
        y.parent = x
        x.parent = p
        x.rightchild = y
        if y == self.root: self.root = x
        else:
            if y == p.leftchild: p.leftchild = x
            else: p.rightchild = x

    def balanceInsert(self, node):
        p = node.parent
        pp = p.parent
        s = pp.rightchild if p == pp.leftchild else pp.leftchild
        if not s.black:
            p.black = s.black = True
            pp.black = False
            if pp == self.root: pp.black = True; return
            else:
                if pp.parent.black: return
                else: self.balanceInsert(pp)
        else:
            if p == pp.leftchild: 
                if node == p.rightchild:
                    self.rotateLeft(p, node)
                    p = node
                self.rotateRight(p, pp)
            else:
                if node == p.leftchild:
                    self.rotateRight(node ,p)
                    p = node
                self.rotateLeft(pp, p)
            p.black = True; pp.black = False

    def balanceDelete(self, p, s):
        x = p.leftchild if s == p.rightchild else p.rightchild
        if not s.black:
            if x == p.leftchild:
                self.rotateLeft(p, s)
                p.black, s.black = False, True
                s = p.rightchild
            else:
                self.rotateRight(s, p)
                p.black, s.black = False, True
                s = p.leftchild
        if s.leftchild.black and s.rightchild.black:
            s.black = False
            if p == self.root or not p.black:
                p.black = True
                return
            np = p.parent
            ns = np.rightchild if p == np.leftchild else np.leftchild
            self.balanceDelete(np, ns)
        else:
            if s == p.rightchild:
                if not s.leftchild.black and s.rightchild.black:
                    l = s.leftchild
                    self.rotateRight(l, s)
                    l.black, s.black = True, False
                    s = l
                self.rotateLeft(p, s)
                s.black = p.black
                p.black = True
                s.rightchild.black = True
            if s == p.leftchild:
                if not s.rightchild.black and s.leftchild.black:
                    r = s.rightchild
                    self.rotateLeft(s, r)
                    r.black, s.black = True, False
                    s = r
                self.rotateRight(s, p)
                s.black = p.black
                p.black = True
                s.leftchild.black = True

    def insert(self, key):
        if key == self.treeSearch(self.root, key).key: return
        r = rbNode(key, False); r.leftchild = self.NIL; r.rightchild = self.NIL
        self.treeInsert(self.root, r)
        if r.parent.black: return
        else: self.balanceInsert(r)

    def delete(self, key):
        target = self.treeSearch(self.root, key)
        if target.leftchild != self.NIL and target.rightchild != self.NIL:
            temp = self.successor(target)
            target.key = temp.key
            target = temp
        if not target.black: self.treeDelete(target)
        else:
            p = target.parent
            s = p.rightchild if target == p.leftchild else p.leftchild
            self.treeDelete(target)
            x = p.leftchild if s == p.rightchild else p.rightchild
            if not x.black:
                x.black = True
                return
            self.balanceDelete(p, s)


if __name__ == '__main__':
    input_arr = [55, 55, 55]
    input_arr1 = [15, 60, 8, 28, 90, 3, 18, 30, 48, 38, 50, 33, 32, 36]
    input_arr2 = [43, 8, 86, 72, 69]
    # bst = BinarySearchTree(55)
    # for num in input_arr1:
    #     bst.insert(num)
    # bst.delete(90)
    # bst.delete(3)
    # bst.delete(28)
    # bst.delete(8)
    # bst.delete(15)
    # bst.delete(60)
    # bst.delete(30)
    # bst.delete(38)
    # bst.printTree()

    rbt = RedBlackTree(55)
    for num in input_arr1:
        rbt.insert(num)
    rbt.printTree()
    rbt.printBlackHeight(rbt.root, 0)
    print()
    erase_arr1 = [28, 90, 3, 55, 8, 15, 50, 60, 30, 38, 18]
    erase_arr2 = [48, 36, 8, 72]
    for num in erase_arr1:
        rbt.delete(num)
        rbt.printTree()
        rbt.printBlackHeight(rbt.root, 0)
        print()
    for num in input_arr2:
        rbt.insert(num)
    rbt.printTree()
    rbt.printBlackHeight(rbt.root, 0)
    print()
    for num in erase_arr2:
        rbt.delete(num)
        rbt.printTree()
        rbt.printBlackHeight(rbt.root, 0)
        print()