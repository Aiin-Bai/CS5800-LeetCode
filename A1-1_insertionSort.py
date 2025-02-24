class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def insertionSort(head):
    
    dummy = Node(0)
    cur = head.next  

    while cur:  
        next_node = cur.next
        prev = dummy
        while prev.next and prev.next.val < cur.val:
            prev = prev.next
        cur.next = prev.next
        prev.next = cur
        cur = next_node

    head.next = dummy.next

## complete this function ##
# Helper functions for testing
def array_to_linked_list(arr):
    head = Node("head")
    cur = head
    for a in arr:
        cur.next = Node(a)
        cur = cur.next
    return head

def print_linked_list(head):
    print("head", end=" -> ")
    cur = head.next
    while cur != None:
        if not cur.next:
            print(cur.val, end="")
        else:
            print(cur.val, end=" -> ")
        cur = cur.next
        print()
# Sample test cases (Please add more test cases)
head = array_to_linked_list([1])
insertionSort(head)
print_linked_list(head) # head -> 1
head = array_to_linked_list([2, 1])
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2
head = array_to_linked_list([1, 2, 3, 4, 5])
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2 -> 3 -> 4 -> 5
head = array_to_linked_list([1, 2, 5, 8, 10, 3, 4, 6, 7, 9])
insertionSort(head)
print_linked_list(head) # head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10


