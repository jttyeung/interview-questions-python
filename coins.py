def coins(num_coins):
    """ Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
    """

    dime = 10
    penny = 1

    def total(total=0):
        total = total + dimes*10 + pennies
        total(total + dime, total + penny)

    change = set()



    if num_coins == 0:
        return change


    coins(num_coins - 1)


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print 'ALL TESTS PASSED!'
