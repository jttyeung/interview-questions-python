def merge_ranges(lst):
    """ Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.

    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    """


if __name__ == '__main__':
    import docttest
    results = docttest.testmod()
    if not results.failed:
        print 'All tests passed!'
