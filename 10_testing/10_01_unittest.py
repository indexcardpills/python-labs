'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

import unittest


def multiply(x, y):
    return x*y-x


print(multiply(2, 4))


# import unittest
# x=2
# y=3
class Testtimes(unittest.TestCase):
     def test_times(self):
        self.assertEqual((multiply(2, 3)), (6))
        self.assertEqual(multiply(3, 10), 30)

     def test_times_two(self):
         self.assertIs(multiply(5, 9), 45, "this failed")
#
if __name__ == '__main__':
    unittest.main()


