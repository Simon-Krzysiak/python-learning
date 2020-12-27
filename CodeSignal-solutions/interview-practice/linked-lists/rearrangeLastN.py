"""Task:
    Given a singly linked list of integers l_list and a non-negative integer
    n, move the last n list nodes to the beginning of the linked list.
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def calc_length(l_list):
    length = 1
    while l_list.next:
        length += 1
        l_list = l_list.next

    return length


def rearrangeLastN(l_list, n):

    if n == 0:
        return l_list

    length = calc_length(l_list)
    if n == length:
        return l_list

    node = l_list

    for _ in range(length - n - 1):
        node = node.next

    head = node.next
    node.next = None
    node = head

    while node.next:
        node = node.next
    node.next = l_list

    return head
