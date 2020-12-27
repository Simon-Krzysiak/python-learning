"""Task:
    Given a binary tree and an integer s, determine whether there is a root
    to leaf path in t such that the sum of vertex values equals s.
"""


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def hasPathWithGivenSum(tree, s):
    if tree is None:
        return False
    elif tree.left is None and tree.right is None:
        return s == tree.value

    return (hasPathWithGivenSum(tree.left, s - tree.value) or
            hasPathWithGivenSum(tree.right, s - tree.value))
