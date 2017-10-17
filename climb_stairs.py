import unittest


def climb_stairs(n):
    """ A fox needs to climb n number of steps. It can jump up 1 step, 2 steps, or 3 steps at a time. How many possible ways are there to get to the top of n steps? """

    if n == 0 or n == 1:
        return 1

    if n == 2:
        return 2

    return climb_stairs(n-1) + climb_stairs(n-2) + climb_stairs(n-3)

# Runtime: O(3^n)


def climb_stairs_dp(n):
    """ A fox needs to climb n number of steps. It can jump up 1 step, 2 steps, or 3 steps at a time. How many possible ways are there to get to the top of n steps? Solve with dynamic programming. """

    cache = { 2: 2, 1: 1, 0: 1 }

    if n in cache:
        return cache[n]

    cache[n] = climb_stairs(n-1) + climb_stairs(n-2) + climb_stairs(n-3)
    return cache[n]

# Runtime: O(n)




class Testing(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(6), 24)
        self.assertEqual(climb_stairs(8), 81)

    def test_climb_stairs_dp(self):
        self.assertEqual(climb_stairs(6), 24)
        self.assertEqual(climb_stairs(8), 81)





if __name__ == '__main__':
    unittest.main()
