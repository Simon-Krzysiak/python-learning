"""Task:
    Given a singly linked list of integers, determine whether or not it's a
    palindrome.
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def isListPalindrome(l_list):
    head1 = l_list
    length = 0
    node = head1

    while hasattr(node, 'next'):
        length += 1
        node = node.next

    half_len, remainder = divmod(length, 2)

    prev_node = None
    node = head1
    for i in range(half_len):
        new_node = node.next
        node.next = prev_node
        prev_node = node
        node = new_node

    node1 = prev_node

    if remainder == 1:
        node = node.next

    node2 = node

    for i in range(half_len):
        if node1.value != node2.value:
            return False
        node1 = node1.next
        node2 = node2.next

    return True
