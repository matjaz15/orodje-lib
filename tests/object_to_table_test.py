import unittest
import os
import sys
sys.path.append('../lib')
cwd = os.getcwd()

from src.lists import object_to_table


class ObjectToTableTest(unittest.TestCase):

    def setUp(self):
       pass
        

    def test_object_to_csv(self):
        self.assertTrue(True)
       
   

if __name__ == '__main__':
    unittest.main()