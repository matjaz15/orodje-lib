import unittest
import os
import sys
sys.path.append('../lib')
cwd = os.getcwd()

from src.lists import object_to_table


class ObjectToTableTest(unittest.TestCase):

    def setUp(self):
        self.object_data_list = [
            {'product_name': 'Eldon Base for stackable storage shelf, platinum', 'company_ids': ['0', '1', '5', '10'], 'contact_name': 'Muhammed MacIntyre', 'group_ids': ['1', '3', '4']},
            {'product_name': '1.7 Cubic Foot Compact "Cube" Office Refrigerators', 'company_ids': ['0', '1'], 'contact_name': False, 'group_ids': ['556', '293', '434', '412']},
            {'product_name': 'Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', 'company_ids': ['0', '1'], 'contact_name': 'Barry French', 'group_ids': '293'},
            {'product_name': 'R380', 'company_ids': ['0', '1', '3'], 'contact_name': 'Clay Rozendal', 'group_ids': '483'}
        ]
        self.expected_list = [
            ['product_name', 'company_ids', 'contact_name', 'group_ids'],
            ['Eldon Base for stackable storage shelf, platinum', '0', 'Muhammed MacIntyre', '1'],
            ['', '1', '', '3'],
            ['', '5', '', '4'],
            ['', '10', '', ''],
            ['1.7 Cubic Foot Compact "Cube" Office Refrigerators', '0', '', '556'],
            ['', '1', '', '293'],
            ['', '', '', '434'],
            ['', '', '', '412'],
            ['Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl', '0', 'Barry French', '293'],
            ['', '1', '', ''],
            ['R380', '0', 'Clay Rozendal', '483'],
            ['', '1', '', ''],
            ['', '3', '', ''],
        ]        

    def test_object_to_csv(self):
        result = object_to_table(
            object_list = self.object_data_list
        )
        self.assertListEqual(self.expected_list, result)
        
       

if __name__ == '__main__':
    unittest.main()