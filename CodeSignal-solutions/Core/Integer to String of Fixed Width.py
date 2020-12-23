def integerToStringOfFixedWidth(number, width):
    string = str(number)
    length = len(string)

    if length < width:
        return ('0'*(width - length)) + string
    elif length == width:
        return string
    else:
        return string[length-width:]
