# with recursions
class Node:
    def __init__(self, value, right, left) -> None:
        self.value = value
        self.right = right
        self.left = left


def printNodes(node: Node, lines: int):

    print(" " * lines + str(node.value))

    if node.right != None:
        lines += 1
        printNodes(node.right, lines)
    if node.left != None:
        lines -= 1
        printNodes(node.left, lines)


def reverseNodes(node: Node):

    if node.right != None and node.left != None:
        node.right, node.left = node.left, node.right
    elif node.right == None and node.left != None:
        node.right, node.left = node.left, None
        reverseNodes(node.left)
    else:
        node.right, node.left = None, node.right
        reverseNodes(node.right)


testNode = Node(3, Node(4, Node(9, None, None), None),
                Node(8, Node(2, None, Node(5, None, None)), Node(6, None, Node(7, None, None))))

printNodes(testNode, 10)
print("\n")
reverseNodes(testNode)
printNodes(testNode, 10)
