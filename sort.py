import unittest
import xmlrunner

class MyTest(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, 1)
        
    def test_example2(self):
        self.assertEqual(2, 1)
        
    def test_example3(self):
        self.assertEqual(6, 6)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))