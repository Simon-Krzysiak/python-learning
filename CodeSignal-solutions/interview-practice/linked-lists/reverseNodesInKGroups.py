"""Task:
    Given a linked list l, reverse its nodes k at a time and return the
    modified list. k is a positive integer that is less than or equal to the
    length of l. If the number of nodes in the linked list is not a multiple
    of k, then the nodes that are left out at the end should remain as-is.

    You may not alter the values in the nodes - only the nodes themselves
    can be changed.
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def length(l_list):
    length = 1
    while l_list.next:
        length += 1
        l_list = l_list.next

    return length


def reverse_k_nodes(head, k):
    prev_node = None
    node = head

    for _ in range(k):
        new_node = node.next
        node.next = prev_node
        prev_node = node
        node = new_node

    return prev_node, new_node, head


def reverseNodesInKGroups(l_list, k):
    nr_groups = length(l_list) // k
    prev_tail = None
    next_head = l_list

    for _ in range(nr_groups):
        new_head, next_head, new_tail = reverse_k_nodes(next_head, k)

        if prev_tail:
            prev_tail.next = new_head
        else:
            new_llist = new_head

        prev_tail = new_tail
        new_tail.next = next_head

    return new_llist
