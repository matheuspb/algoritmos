def check_ii(vector, offset=0):
    print(vector)
    middle = len(vector)//2

    if len(vector) == 1:
        return vector[0] == offset
    elif vector[middle] - offset == middle:
        return True
    elif vector[middle] - offset < middle:
        return check_ii(vector[middle:], offset + middle)
    else:
        return check_ii(vector[:middle], offset)
