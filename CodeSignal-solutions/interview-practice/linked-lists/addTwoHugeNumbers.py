"""Task:
   You're given 2 huge integers represented by linked lists. Each linked
   list element is a number from 0 to 9999 that represents a number with
   exactly 4 digits. The represented number might have leading zeros. Your
   task is to add up these huge integers and return the result in the same
   format.
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverse_and_count(l_list):
    prev_node = None
    node = l_list
    count = 0

    while hasattr(node, 'next'):
        new_node = node.next
        node.next = prev_node
        prev_node = node
        node = new_node
        count += 1

    return prev_node, count


def addTwoHugeNumbers(a, b):
    list1, len1 = reverse_and_count(a)
    list2, len2 = reverse_and_count(b)

    if len2 > len1:
        list2, list1 = list1, list2
        len2, len1 = len1, len2
    head = list1
    node = list1
    node2 = list2
    rem = 0

    while hasattr(node, 'next'):
        nr1 = node.value + rem
        nr2 = 0

        if hasattr(node2, 'value'):
            nr2 = node2.value
            node2 = node2.next
        rem, node.value = divmod(nr1+nr2, 10000)
        if node.next is None and rem == 1:
            tail = ListNode(rem)
            node.next = tail
            rem = 0
        else:
            node = node.next

    return reverse_and_count(head)[0]
