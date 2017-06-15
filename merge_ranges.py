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

    >>> merge_ranges([(0, 3), (3, 5), (7, 8)])
    [(0, 5), (7, 8)]

    >>> merge_ranges([(1, 5), (2, 3)])
    [(1, 5)]
    """

    # if each tuple is (x, y),
    # find the min x, and see if its y matches any other x.
        # if it does, then look at that y, and see if it is >= an x
        # otherwise, add that tuple to a new list
        # and look at the next lowest min


    # time: O(nlogn)
    # space: O(n)

    set_times = sorted(lst)

    merged_range = []

    n = 0
    start = 0

    while start < len(set_times) - 1:
        a = set_times[start][n]
        b = set_times[start][n+1]

        for i, t in enumerate(set_times):
            if b >= t[0] and t[1] >= b:
                b = t[1]
                start = i + 1
            n = i + 1

        n = 0
        merged_range.append((a, b))




    # set_times = [(0, 3), (3, 5)]
    # len = 2
    # n = 0
    # a = 0
    # b = 3
    # t[0] = 0, t[1] = 3
    # n = 1
    # t[0] = 3, t[1] = 5
    # 3 >= 3:
    # b = 5
    # n = 2
    # merged_range = [(0, 5)]


    # set_times = [(0, 3), (3, 5), (7, 8)]
    # len = 3
    # n = 0
    # start = 0
    # a = 0
    # b = 3
    # t[0] = 0, t[1] = 3
    # n = 1
    # t[0] = 3, t[1] = 5
    # 3 >= 3:
    # b = 5
    # start = 2
    # n = 2
    # t[0] = 7, t[1] = 8
    # n = 0
    # merged_range = [(0, 5)]
    # start 2 < 3 len
    # a = 7
    # b = 8
    #








    return merged_range








if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if not results.failed:
        print 'All tests passed!'
