import unittest
from src.misc.NameGenerator import name_generator

class NameGenTesting(unittest.TestCase):
    def test_name_gen(self):
        name = name_generator()
        name2 = name_generator()

        self.assertTrue(name, str)
        self.assertNotEqual(name, name2)