def merge_ranges(lst):
    """ In HiCal, a meeting is stored as tuples of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am. For example:
    (2, 3) # meeting from 10:00 - 10:30 am
    (6, 9) # meeting from 12:00 - 1:30 pm
    Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.

    >>> merge_ranges([(3, 5), (4, 8), (10, 12), (9, 10), (0, 1)])
    [(0, 1), (3, 8), (9, 12)]

    >>> merge_ranges([(0, 3), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 8), (9, 12)]

    >>> merge_ranges([(0, 3), (3, 5)])
    [(0, 5)]
    """

    # if each tuple is (x, y),
    # find the min x, and see if its y matches any other x.
        # if it does, then look at that y, and see if it is >= an x
        # otherwise, add that tuple to a new list
        # and look at the next lowest min

    # sorted_times = sorted(lst)




    # for i, t in enumerate(sorted_times):
    #     x = t[0]
    #     y = t[1]
    #     if min(x) == x:
    #         if y >= x:
    #             x ==

    set_lst = set(lst)

    merged_range = []

    for i, t in enumerate(set_lst):
        start = min(set_lst)
        x, y = start

        if y >= t[1]:
            y = t[0]
        else:
            merged_range.append((x,y))
            set_lst.remove(t)

    # set_lst = set(([(3, 5), (4, 8), (10, 12), (9, 10), (0, 1)]))
    # i = 0
    # t = (3, 5)
    # start = (0, 1)
    # x = 0, y = 1
    # if 1 >= 0




    return merged_range








if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if not results.failed:
        print 'All tests passed!'
