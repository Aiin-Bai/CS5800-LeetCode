## Q1
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def mergeTwoLinkedLists(A, B):
## Complete this function ##
    if A and A.val == "head":
        A = A.next
    if B and B.val == "head":
        B = B.next
    dummyNode = Node("head")
    cur = dummyNode
    while A and B:
        if A.val < B.val:
            cur.next = A
            A = A.next
        else:
            cur.next = B
            B = B.next
        cur = cur.next
    if A:
        cur.next = A
    else:
        cur.next = B
    return dummyNode
    
# Helper functions for testing
def array_to_linked_list(arr):
    head = Node("head")
    cur = head
    for i in arr:
        cur.next = Node(i)
        cur = cur.next
    return head
def print_linked_list(head):
    if head.val == "head":
        print("head", end=" -> ")
    else:
        raise Exception("The linked list is malformed")
    cur = head.next
    while cur:
        if not cur.next:
            print(cur.val, end="")
        else:
            print(cur.val, end=" -> ")
        cur = cur.next
print()

A = array_to_linked_list([2, 4, 5, 7])
B = array_to_linked_list([1, 2, 3, 6])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 1 -> 2 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
A = array_to_linked_list([1, 3, 5, 7])
B = array_to_linked_list([])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 1 -> 3 -> 5 -> 7
A = array_to_linked_list([])
B = array_to_linked_list([2, 4, 6, 8])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 2 -> 4 -> 6 -> 8
A = array_to_linked_list([2])
B = array_to_linked_list([2, 4, 6, 8])
print_linked_list(mergeTwoLinkedLists(A, B))
# head -> 2 -> 2 -> 4 -> 6 -> 8

A = array_to_linked_list([])
B = array_to_linked_list([])
print_linked_list(mergeTwoLinkedLists(A,B))
# head->






## Q2
def maxSubArray(A:list):
## complete this function ##
    curSum = A[0]
    maxSum = A[0]
    start = 0
    tmpStart = 0
    end = 0
    for index, val  in enumerate(A[1:],start=1):
        if val> curSum+val:
            curSum = val
            tmpStart = index
        else:
            curSum+=val

        if curSum> maxSum:
            maxSum = curSum
            start = tmpStart
            end = index

    return A[start:end+1], maxSum

print(maxSubArray([-100])) # returns ([-100], -100)
print(maxSubArray([13, -100, 20]) )# returns ([20], 20)
print(maxSubArray([-100, 20, -10, 60, 80])) # returns ([20, -10, 60, 80], 150)
print(maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
# returns ([18, 20, -7, 12], 43)
print(maxSubArray([1,2,3,-500000,1]))
#return ([1,2,3])
