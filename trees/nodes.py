class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def in_order_traversal(r):
    if r is None:
        return

    # traverse left subtree
    in_order_traversal(r.getLeftChild())
    # print node
    print(r.getRootVal())
    # traverse right subtree
    in_order_traversal(r.getRightChild())
    return

if __name__ == "__main__":

    r = BinaryTree("a")
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())

    r1 = BinaryTree("a")
    r1.insertLeft("b")
    r1.getLeftChild().insertRight("d")
    r1.insertRight("c")
    r1.getRightChild().insertLeft("e")
    r1.getRightChild().insertRight("f")

    in_order_traversal(r1)
