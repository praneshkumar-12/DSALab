from LinkedBinaryTree import LinkedBinaryTree


def main():
    tree = LinkedBinaryTree()
    tree.addRoot("a")
    tree.addLeft("b")
    tree.addRight("c")
    print(tree)
    tree.addLeft("d", tree.root.left)
    tree.addRight("e", tree.root.left)
    tree.addLeft("f", tree.root.right)
    tree.addRight("g", tree.root.right)
    print(tree)
    tree.mirror(tree.root)
    print(tree)

if __name__ == "__main__":
    main()
    