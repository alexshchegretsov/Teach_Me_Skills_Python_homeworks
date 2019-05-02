import unittest
import test_clss

myTimeTestSuite = unittest.TestSuite()
myTimeTestSuite.addTest(unittest.makeSuite(test_clss.LogicOperationsMyTime))
myTimeTestSuite.addTest(unittest.makeSuite(test_clss.CalcMyTime))
myTimeTestSuite.addTest(unittest.makeSuite(test_clss.MethodsMyTime))
print(f"count of tests: {str(myTimeTestSuite.countTestCases())}\n")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(myTimeTestSuite)
