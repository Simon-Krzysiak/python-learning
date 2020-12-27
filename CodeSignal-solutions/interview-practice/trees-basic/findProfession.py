"""Task:
    Consider a special family of Engineers and Doctors. This family has the
    following rules:

    - Everybody has two children.
    - The first child of an Engineer is an Engineer and the second child is
        a Doctor.
    - The first child of a Doctor is a Doctor and the second child is an
        Engineer.
    - All generations of Doctors and Engineers start with an Engineer.

    Given the level and position of a person in the ancestor tree above,
    find the profession of the person.
    Note: in this tree first child is considered as left child, second - as
    right.
"""


def findProfession(level, pos):
    nr_ones = bin(pos-1).count('1')
    if nr_ones % 2 == 1:
        return 'Doctor'
    else:
        return 'Engineer'
