class Node:
    def __init__(self, v, p=None, l=None, r=None, h=0):
        self.left = l
        self.right = r
        self.parent = p
        self.value = v
        self.height = h

class AVLTree:
    def __init__(self):
        self.root = None

    def print(self):
        def print_helper(root, depth):
            tab = " " * (depth * 5)
            if not root:
                print(tab, "None")
                return
            print_helper(root.right, depth + 1)
            print(tab + str(root.value) + "(" + str(root.height) + ")")
            print_helper(root.left, depth + 1)
        
        if self.root:
            print_helper(self.root, 0)
        else:
            print("Tree is empty")

    def leftRotate(self, x):

        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.updateHeight(x)
        self.updateHeight(y)
        return y  

    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        self.updateHeight(y)
        self.updateHeight(x)
        return x 

    def getHeight(self, node):
        return node.height if node else -1

    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    def updateHeight(self, node):
        if node:
            node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    def rebalance(self, node):
        """ 重新平衡 AVL 树，并返回新的根节点 """
        self.updateHeight(node)
        balance = self.getBalance(node)

        # LL Case
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)

        # LR Case
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # RR Case
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)

        # RL Case
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node  # ⚠️ 必须返回新的根节点

    def insert(self, v):
        """ 插入新值 """
        def _insert(node, v):
            if not node:
                return Node(v)
            elif v < node.value:
                node.left = _insert(node.left, v)
                node.left.parent = node
            else:
                node.right = _insert(node.right, v)
                node.right.parent = node

            return self.rebalance(node)  # ⚠️ 关键：确保返回新的根节点

        if not self.root:
            self.root = Node(v)
        else:
            self.root = _insert(self.root, v)  # ⚠️ 更新根节点

    def delete(self, v):
        """ 删除节点 """
        def _delete(node, v):
            if not node:
                return node

            # 递归查找要删除的节点
            if v < node.value:
                node.left = _delete(node.left, v)
            elif v > node.value:
                node.right = _delete(node.right, v)
            else:
                # 叶子节点或只有一个子节点
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    return temp

              
                temp = self.getMinValueNode(node.right)
                node.value = temp.value  
                node.right = _delete(node.right, temp.value)  

            return self.rebalance(node) 

        self.root = _delete(self.root, v) 

    def getMinValueNode(self, node):
       
        while node and node.left:
            node = node.left
        return node

# Helper function for testing
def arrayToBST(nums):
    tree = AVLTree()
    for n in nums:
        tree.insert(n)
    tree.print()
    print("-----------------------------------------------")
    return tree


tree = arrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("--- deleting 3")
tree.delete(3)
tree.print()

print("--- deleting 1")
tree.delete(1)
tree.print()

print("--- deleting 10")
tree.delete(10)
tree.print()

########
# Test Case 1: 
print("\nTest Case 1: Decreasing sequence")
tree = arrayToBST([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

print("--- deleting middle node 5")
tree.delete(5)
tree.print()

print("--- deleting leaf node 1")
tree.delete(1)
tree.print()

print("--- deleting root node")
tree.delete(6)
tree.print()

# Test Case 2: 
print("\nTest Case 2: Multiple rotations after deletion")
tree = arrayToBST([5, 3, 8, 2, 4, 7, 9])

print("--- deleting 2 (triggers rebalancing)")
tree.delete(2)
tree.print()

print("--- deleting 3 (triggers double rotation)")
tree.delete(3)
tree.print()

# Test Case 3
print("\nTest Case 3: Empty tree and single node operations")
tree = AVLTree()
print("Empty tree:")
tree.print()

print("--- inserting single node")
tree.insert(1)
tree.print()

print("--- deleting from single node tree")
tree.delete(1)
tree.print()

# Test Case 4
print("\nTest Case 4: Duplicate values")
tree = arrayToBST([5, 5, 3, 3, 7, 7])

print("--- deleting first 5")
tree.delete(5)
tree.print()

print("--- deleting second 5")
tree.delete(5)
tree.print()

# Test Case 5: zigzag 
print("\nTest Case 5: Zigzag pattern")
tree = arrayToBST([10, 5, 15, 3, 7, 13, 17, 4, 6, 8])

print("--- deleting nodes to trigger complex rotations")
tree.delete(15)
tree.print()
tree.delete(5)
tree.print()
tree.delete(7)
tree.print()