"""Task:
    Given an array of integers nums and an integer k, determine whether
    there are two distinct indices i and j in the array where nums[i] =
    nums[j] and the absolute difference between i and j is less than or
    equal to k.
"""


def containsCloseNums(nums, k):

    indices = dict()
    for i in range(len(nums)):
        indices.setdefault(nums[i], []).append(i)

    for nr in indices:
        vals = indices[nr]
        for i in range(1, len(vals)):
            for j in range(i):
                if abs(vals[i] - vals[j]) <= k:
                    return True

    return False
