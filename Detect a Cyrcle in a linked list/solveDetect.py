class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def hasCycle(head):
    slowPointer, fastPointer = head, head
    
    while slowPointer is not None and fastPointer is not None and fastPointer.next is not None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        
        if slowPointer == fastPointer:
            return True  # If the pointers meet, there is a cycle

    return False  # There is no cycle if the loop ends without two pointers meeting


# Test Function
def test_hasCycle():
    # test in case there is no cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(hasCycle(node1))  # waiting: False

    # test in case there is cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # create Cycle

    print(hasCycle(node1))  # waiting: True


test_hasCycle()
