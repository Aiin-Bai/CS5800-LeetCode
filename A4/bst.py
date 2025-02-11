class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        cur = self.root
        while cur:
            if cur.value == key:
                print("The given key already exists:", key)
                return
            elif cur.value > key:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(key)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(key)
                    return

    def k_largest(self, k):
        if not self.root:
            print("The tree is empty!")
            return None
        
        self.count = 0
        self.result = None
        self.reverse_inorder(self.root, k)

        if self.result is None:
            print(f"The tree has less than {k} nodes!")
        return self.result

    def reverse_inorder(self, node, k):
        if not node or self.count >= k:
            return

        self.reverse_inorder(node.right, k)

        self.count += 1
        if self.count == k:
            self.result = node.value

        self.reverse_inorder(node.left, k)    

   
# Helper function for testing
def arrayToBST(nums):
    tree = BST()
    for n in nums:
        tree.insert(n)
    return tree


# Test cases. Please add your own test cases too.
t1 = arrayToBST([41, 20, 65, 11, 29, 50, 91, 32, 72, 99])
t1.k_largest(4) # returns 65
t1.k_largest(1) # returns 99
t1.k_largest(10) # returns 11
t1.k_largest(11) # prints "The tree has less than 11 nodes!" and returns None

t2 = arrayToBST([6, 3, 8, 1, 5, 7, 9])
t2.k_largest(3) # returns 7
t3 = arrayToBST([])
t3.k_largest(5) # prints "The tree is empty!" and returns None

#####
t4 = arrayToBST([41, 20, 65, 11, 29, 50, 91, 32, 72, 99])
t4.k_largest(0)  #  "Invalid input: k should be greater than 0!"
t5 = arrayToBST([1,2,3,4])
t5.k_largest(20) #"The tree has less than 20 nodes!" and returns None