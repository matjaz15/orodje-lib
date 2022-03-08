import unittest
import os
import sys
sys.path.append('../lib')
cwd = os.getcwd()

from src.lists import object_to_table


class ObjectToTableTest(unittest.TestCase):

    def setUp(self):
        self.object_list = [
            {'product_name': 'Eldon Base for stackable storage shelf, platinum', 'contact_name': 'Muhammed MacIntyre', 'group_ids': ['1', '3', '4']},
            {'product_name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'contact_name': False, 'group_ids': ['556', '293', '434', '412']},
            {'product_name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'contact_name': 'Barry French', 'group_ids': '293'},
            {'product_name': 'R380', 'contact_name': 'Clay Rozendal', 'group_ids': '483'}
        ]
        self.expected_list = [
            ['product_name', 'contact_name', 'group_ids'],
            ['Eldon Base for stackable storage shelf, platinum', 'Muhammed MacIntyre', '1'],
            ['', '', '3'],
            ['', '', '4'],
            ['1.7 Cubic Foot Compact "Cube" Office Refrigerators', '', '556'],
            ['', '', '293'],
            ['', '', '434'],
            ['', '', '412'],
            ['Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'Barry French', '293'],
            ['R380', 'Clay Rozendal', '483'],
        ]        

    def test_object_to_csv(self):
        result = object_to_table(
            object_list = self.object_list
        )
        self.assertListEqual(self.expected_list, result)
        
       

if __name__ == '__main__':
    unittest.main()