def addBorder(picture):
    length = len(picture[0]) + 2
    framed = list()
    framed.append('*' * length)

    for row in picture:
        framed.append('*' + row + '*')
    framed.append('*' * length)

    return framed
