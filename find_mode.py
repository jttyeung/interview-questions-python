def find_mode(arr):
    """ Finds the mode(s) of the array.

    >>> sorted(find_mode([3,5,6,2,6,7,8,3,6,6]))
    [3, 6]

    >>> find_mode([1,2,3,4,5])
    []

    >>> sorted(find_mode([2,1,2,1]))
    [1, 2]

    >>> find_mode([1,2,3,2,4])
    [2]

    >>> find_mode([])
    []

    """

    if not arr:
        return []
    if len(arr) < 2:
        return arr[0]

    nums = {}

    for i in arr:
        nums[i] = nums.get(i, 0) + 1

    return [letter for letter, val in nums.iteritems() if val > 1]





if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print "ALL TESTS PASSED!"
