import unittest
from module1 import Good
import pandas as pd
import sklearn as sk
import sklearn as tp
import CSV as lp
import module1 as ms

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('fo5'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_module1(self):
        k=Good()
        answer=k.example1()
        self.assertEqual(answer, 2)

if __name__ == '__main__':  
    unittest.main() #allows the results of the test to be displayed when run from the command line