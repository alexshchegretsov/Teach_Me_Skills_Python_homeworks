import unittest
import test_hw_15_task_2

figureTestSuite = unittest.TestSuite()
figureTestSuite.addTest(unittest.makeSuite(test_hw_15_task_2.distanceFigure))
figureTestSuite.addTest(unittest.makeSuite(test_hw_15_task_2.calcPerimeter))
figureTestSuite.addTest(unittest.makeSuite(test_hw_15_task_2.calcSquare))
print(f'count of tests: {str(figureTestSuite.countTestCases())}\n')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(figureTestSuite)
