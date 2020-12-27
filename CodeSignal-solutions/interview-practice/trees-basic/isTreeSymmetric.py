"""Task:
    Given a binary tree, determine whether it is symmetric around its
    center, i.e. each side mirrors the other.
"""


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def sublevel(parents):
    if parents == [None]:
        return None
    children = list()
    for parent in parents:
        if parent:
            children.append(parent.left)
            children.append(parent.right)
    return children


def values(level):
    vals = list()
    for node in level:
        if node:
            vals.append(node.value)
        else:
            vals.append(None)
    return vals


def isTreeSymmetric(tree):
    if not tree:
        return True
    left = [tree.left]
    right = [tree.right]

    while left and right:
        if values(left) != values(right)[::-1]:
            return False
        left = sublevel(left)
        right = sublevel(right)

    return True
