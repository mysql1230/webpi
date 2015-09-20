import glob
import os
import sys
import unittest

if __name__ == '__main__':
    PATH =os.path.dirname(os.path.realpath(__file__))
    sys.path.append(PATH)
    sys.path.append(PATH + '/..')
    os.chdir(PATH)
    test_files = glob.glob('test_*.py')
    
    modules = [f[0:len(f)-3] for f in test_files]
    suites = [unittest.defaultTestLoader.loadTestsFromName(m) for m in modules]
    testSuite = unittest.TestSuite(suites)
    text_runner = unittest.TextTestRunner().run(testSuite)