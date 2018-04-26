def remove_duplicates(vector):
    if len(vector) == 1:
        return vector

    left = remove_duplicates(vector[:len(vector)//2])
    right = remove_duplicates(vector[len(vector)//2:])

    return merge(left, right)

def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        elif left[0] > right[0]:
            result.append(right.pop(0))
        else:
            while left and right and left[0] == right[0]:
                right.pop(0)
            result.append(left.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result
