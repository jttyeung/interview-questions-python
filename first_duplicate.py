def first_duplicate(a):
    """

    >>> first_duplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])
    6

    # O()

    lowest_index = len(a)
    for i in range(len(a)):
        num = a[i]
        if num in a[i+1:]:
            index = a[i+1:].index(num) + i + 1
            if index < lowest_index:
                lowest_index = index

    if lowest_index < len(a):
        return a[lowest_index]


    return -1

