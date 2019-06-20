import unittest
import simplemath as sm

class TestSimpleMAth(unittest.TestCase):
    def test_add(self):
        ret = sm.add(1,3)
        self.asserEqual(ret, 4)

    def test_add_negint(self):
        ret = sm.add(-1,-3)
        self.assertEqual(ret, -4)

    def test_add_string(self):
        ret = sm.add('a','b')
        self.assertEqual(ret, 'ab')

if __name__ == "__main__":
    unittest.main()

