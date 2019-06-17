class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def left(self, left):
        self.left = left

    def right(self, right):
        self.right = right


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
a.left = b
a.right = c

b.left = d
b.right = e
c.right = f
f.left = g
print(a.name, a.left.name, a.left.right.name)

# def printBasic(node):
#   while node:


print("******")


def printBasic(ns):
    print("printBasic")
    for list in ns:
        for n in list:
            print(n.name, end=" ")
        print("")


# printBasic([[a], [b, c] , [d, f, g]])

def printNodes(node):
    print("printNodes")
    a = []
    a.append(node)
    parent = [a]
    while len(parent) > 0:
        # print("test")
        ns = parent.pop(0)
        # print(ns)
        child = []
        # print(len(ns))
        for n in ns:
            print(n.name, end=" ")
            # print(n.name, end=" ")
            if n.left:
                child.append(n.left)
            if n.right:
                child.append(n.right)

        if len(child) > 0:
            parent.append(child)
        print(" ")


printNodes(a)
