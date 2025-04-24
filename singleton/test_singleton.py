# singleton/test_singleton.py

import unittest
from singleton import Singleton

class TestSingleton(unittest.TestCase):
    def test_single_instance(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertIs(s1, s2)

    def test_shared_state(self):
        s1 = Singleton()
        s2 = Singleton()
        s1.increment()
        s2.increment()
        self.assertEqual(s1.get_value(), 2)
        self.assertEqual(s2.get_value(), 2)

if __name__ == "__main__":
    unittest.main()
