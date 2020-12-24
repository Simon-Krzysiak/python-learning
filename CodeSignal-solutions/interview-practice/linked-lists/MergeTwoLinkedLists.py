"""Task:
    Given two singly linked lists sorted in non-decreasing order, your task
    is to merge them. In other words, return a singly linked list, also
    sorted in non-decreasing order, that contains the elements from both
    original lists.
 """

import math


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1

    head = ListNode(0)
    if list1.value <= list2.value:
        head.value = list1.value
        list1 = list1.next
    else:
        head.value = list2.value
        list2 = list2.next

    node = head

    while hasattr(list1, 'value') or hasattr(list2, 'value'):
        if hasattr(list1, 'value'):
            val1 = list1.value
        else:
            val1 = math.inf

        if hasattr(list2, 'value'):
            val2 = list2.value
        else:
            val2 = math.inf

        if val1 <= val2:
            node.next = list1
            node = list1
            list1 = list1.next
        else:
            node.next = list2
            node = list2
            list2 = list2.next

    return head
