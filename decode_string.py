def decode(s):
    """ Decodes a string. A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

    Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'
    Longer patterns should work:

    >>> decode("0h1ae2bcy")
    'hey'
    """

