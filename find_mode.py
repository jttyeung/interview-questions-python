def find_mode(arr):
    """ Finds the mode(s) of the array.

    >>> find_mode([3,5,6,2,6,7,8,3,6,6])
    6

    >>> find_mode([1,2,3,4,5])
    None

    >>> find_mode([2,1,2,1])
    [2,1]

    >>> find_mode([1,2,3,2,4])
    2

    >>> find_mode([])
    None

    """





if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print "ALL TESTS PASSED!"
