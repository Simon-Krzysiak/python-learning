"""Task:
    Given a singly linked list of integers l_list and an integer k, remove
    all elements from list l that have a value equal to k."""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l_list, k):

    head = l_list
    while hasattr(head, 'next'):
        if head.value == k:
            head = head.next
        else:
            break

    node = head
    prev_node = head

    while hasattr(node, 'next'):
        next_node = node.next
        if node.value == k:
            prev_node.next = next_node
            node = next_node
        else:
            prev_node = node
            node = next_node
    return head
