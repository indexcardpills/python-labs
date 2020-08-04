'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

import unittest


def subtract(a, b):
    return a-b

def remainder(x, y):
    return x%y



class Testing(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(9,8), (2))

    def test_remainder(self):
        self.assertEqual(remainder(10, 6), (4))

unittest.main()