import unittest
from task import main
import subprocess
import sys
from test_helper import failed, passed
from UserInputHelper import *

helper = Helper()


class varAanmaken(unittest.TestCase):
    def testCondition1(self):
        proc = subprocess.run([sys.executable, "-c", "import task; task.main(17)"], stdout=subprocess.PIPE)
        arr = []
        with proc.stdout():
            for line in iter(proc.stdout.readline, b''):
                arr.append(line)
        proc.wait()
        self.assertEqual(arr, [b'Reduction = 10%\r\n'])

    def testCondition2(self):
        pass
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=varAanmaken)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        passed("Congratulations")
    else:
        for el in res.failures:
            failed(f"There is an error in " + str(el[0])[4:14])




