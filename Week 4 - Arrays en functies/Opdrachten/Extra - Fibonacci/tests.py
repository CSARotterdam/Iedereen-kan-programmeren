import unittest
import task
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    @staticmethod
    def fibo(n):
        if n <= 1:
            return n
        else:
            return varAanmaken.fibo(n - 1) + varAanmaken.fibo(n - 2)

    def testFibonacciSequenceShouldBeImplementedCorrectly(self):
        for n in range(30):
            self.assertEqual(varAanmaken.fibo(n), task.Fibonacci(n))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"The following condition is not met: " + str(el[0])[4:-23])




