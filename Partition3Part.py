class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def partitionLinkedList(head):
## Complete this function ##
    
    if not head or not head.next:
        return head
    pivot = head.next  
    pivot_val = pivot.val

    small_dummy = Node(0)
    equal_dummy = Node(0)
    large_dummy = Node(0)
    
    small_tail = small_dummy
    equal_tail = equal_dummy
    large_tail = large_dummy

    cur = head.next
    while cur:
        if cur.val < pivot_val:
            small_tail.next = cur
            small_tail = small_tail.next
        elif cur.val > pivot_val:
            large_tail.next = cur
            large_tail = large_tail.next
        else:  
            equal_tail.next = cur
            equal_tail = equal_tail.next
        cur = cur.next

    small_tail.next = None
    equal_tail.next = None
    large_tail.next = None
    
    if small_dummy.next:
        new_head = small_dummy.next
        small_tail.next = equal_dummy.next  
    else:
        new_head = equal_dummy.next  
    equal_tail.next = large_dummy.next 
    

    
    head.next = new_head
    return head
        
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
# sample test cases
LL = array_to_linked_list([1])
print_linked_list(partitionLinkedList(LL)) # head -> 1
LL = array_to_linked_list([1, 1, 1])
print_linked_list(partitionLinkedList(LL)) # head -> 1 -> 1 -> 1
LL = array_to_linked_list([2, 1, 3, 2, 1, 3])
print_linked_list(partitionLinkedList(LL)) # head -> 1 -> 1 -> 2 -> 2 -> 3 -> 3
LL = array_to_linked_list([2, 4, 5, 7])
print_linked_list(partitionLinkedList(LL)) # head -> 2 -> 4 -> 5 -> 7
LL = array_to_linked_list([7, 4, 5, 2])
print_linked_list(partitionLinkedList(LL)) # head -> 4 -> 5 -> 2 -> 7
LL = array_to_linked_list([6, 2, 7, 9, 3, 1, 5, 2, 6, 7, 3])
print_linked_list(partitionLinkedList(LL))
# head -> 2 -> 3 -> 1 -> 5 -> 2 -> 3 -> 6 -> 6 -> 7 -> 9 -> 7

LL = array_to_linked_list([])
print_linked_list(partitionLinkedList(LL))

LL = array_to_linked_list([3,3,5,7])
print_linked_list(partitionLinkedList(LL))
# head ->3 -> 3 -> 5 -> 7

LL = array_to_linked_list([3,3,2,1])
print_linked_list(partitionLinkedList(LL))
# head ->2 -> 1 -> 3 -> 3